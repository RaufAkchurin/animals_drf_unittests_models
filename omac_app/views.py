from django.shortcuts import render
from rest_framework import viewsets

from omac_app.models import AnimalType, Breed, Animal
from omac_app.serializer import AnimalTypeSerializer, BreedSerializer, AnimalSerializer


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
