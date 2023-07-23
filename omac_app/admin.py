from django.contrib import admin

from omac_app.models import AnimalType, Breed, Animal, Weighting

# Register your models here.
admin.site.register(AnimalType)
admin.site.register(Breed)
admin.site.register(Animal)
admin.site.register(Weighting)
