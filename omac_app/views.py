from django.shortcuts import render
from rest_framework import viewsets

from omac_app.models import AnymalType
from omac_app.serializer import AnimalTypeSerializer


# Create your views here.

class TypeView(viewsets.ModelViewSet):
    serializer_class = AnimalTypeSerializer
    queryset = AnymalType.objects.all()
