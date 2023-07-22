from django.db import models


class AnimalType(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Breed(models.Model):
    name = models.CharField(max_length=10)
    type = models.OneToOneField(
        "AnimalType",
        on_delete=models.PROTECT,
    )

    def __str__(self):
        return self.name
