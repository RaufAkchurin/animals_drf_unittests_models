from django.shortcuts import render
from rest_framework import viewsets

from omac_app.models import AnimalType, Breed
from omac_app.serializer import AnimalTypeSerializer, BreedSerializer


# Create your views here.

class TypeView(viewsets.ModelViewSet):
    serializer_class = AnimalTypeSerializer
    queryset = AnimalType.objects.all()


class BreedView(viewsets.ModelViewSet):
    serializer_class = BreedSerializer
    queryset = Breed.objects.all()
