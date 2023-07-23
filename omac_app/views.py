from django.shortcuts import render
from rest_framework import viewsets

from omac_app.models import AnimalType, Breed, Animal, Weighting
from omac_app.serializer import AnimalTypeSerializer, BreedSerializer, AnimalSerializer, WeightingSerializer


# Create your views here.

class TypeView(viewsets.ModelViewSet):
    serializer_class = AnimalTypeSerializer
    queryset = AnimalType.objects.all()


class BreedView(viewsets.ModelViewSet):
    serializer_class = BreedSerializer
    queryset = Breed.objects.all()


class AnimalView(viewsets.ModelViewSet):
    serializer_class = AnimalSerializer
    queryset = Animal.objects.all()


class WeightingView(viewsets.ModelViewSet):
    serializer_class = WeightingSerializer
    queryset = Weighting.objects.all()
