import datetime

from rest_framework import serializers

from omac_app.models import AnimalType, Breed, Animal, Weighting


class AnimalTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimalType
        fields = (
            "id",
            "name",
        )


class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = (
            "id",
            "name",
            "type",
        )


class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = (
            "id",
            "inventory_num",
            "sex",
            "nickname",
            "arrival_date",
            "arrival_age",
            "breed",
            "parent",
        )


class WeightingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weighting
        fields = (
            "id",
            "animal",
            "date",
            "weight",
        )

    def validate(self, data):
        animal = data.get('animal')
        date = data.get('date')

        # If it's an update, exclude the current instance from the uniqueness check
        instance = self.instance
        if instance and instance.animal == animal and instance.date == date:
            return data

        if Weighting.objects.filter(animal=animal, date=date).exists():
            raise serializers.ValidationError("One weighting to this animal per day")
        return data
