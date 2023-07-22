from rest_framework import serializers

from omac_app.models import AnimalType, Breed


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