from rest_framework import serializers

from omac_app.models import AnymalType


class AnimalTypeSerializer(serializers.ModelSerializer):
    name = serializers.CharField()

    class Meta:
        model = AnymalType
        fields = (
            "id",
            "name",
        )
