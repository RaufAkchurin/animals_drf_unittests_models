from django.contrib import admin

from omac_app.models import AnimalType, Breed

# Register your models here.
admin.site.register(AnimalType)
admin.site.register(Breed)
