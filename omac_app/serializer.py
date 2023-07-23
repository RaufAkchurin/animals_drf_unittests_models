import datetime

from rest_framework import serializers

from omac_app.models import AnimalType, Breed, Animal, Weighting


class AnimalTypeSerializer(serializers.ModelSerializer):
    name = serializers.CharField()

    class Meta:
        model = AnimalType
        fields = (
            "id",
            "name",
        )


class BreedSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    type = serializers.PrimaryKeyRelatedField(queryset=AnimalType.objects.all())

    class Meta:
        model = Breed
        fields = (
            "id",
            "name",
            "type",
        )


class AnimalSerializer(serializers.ModelSerializer):
    number = serializers.IntegerField()
    sex = serializers.ChoiceField(choices=Animal.SEX_CHOICES)
    nickname = serializers.CharField(max_length=50)
    arrival_date = serializers.DateField()
    arrival_age = serializers.IntegerField(min_value=0, max_value=25)
    breed = serializers.PrimaryKeyRelatedField(queryset=Breed.objects.all())
    parent = serializers.PrimaryKeyRelatedField(queryset=Animal.objects.all(), required=False)

    class Meta:
        model = Animal
        fields = (
            "id",
            "number",
            "sex",
            "nickname",
            "arrival_date",
            "arrival_age",
            "breed",
            "parent",
        )

    def validate_number(self, value):
        if self.instance is None and Animal.objects.filter(number=value).exists():  # only for create without update
            raise serializers.ValidationError("This value already exists. Please choose a unique value.")
        return value


class WeightingSerializer(serializers.ModelSerializer):
    animal = serializers.PrimaryKeyRelatedField(queryset=Animal.objects.all())
    date = serializers.DateField()
    weight = serializers.IntegerField()

    class Meta:
        model = Weighting
        fields = (
            "animal",
            "date",
            "weight",
        )

    def validate(self, data):
        animal = data.get('animal')
        date = data.get('date')

        if Weighting.objects.filter(animal=animal, date=date).exists():
            raise serializers.ValidationError("One weighting to animal per day")
        return data
