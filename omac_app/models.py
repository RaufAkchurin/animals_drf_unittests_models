from django.db import models


class AnimalType(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Breed(models.Model):
    name = models.CharField(max_length=10)
    type = models.ForeignKey(
        "AnimalType",
        on_delete=models.PROTECT,
    )

    def __str__(self):
        return self.name


class Animal(models.Model):
    SEX_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    number = models.IntegerField(unique=True)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    nickname = models.CharField(max_length=50)
    arrival_date = models.DateField()
    arrival_age = models.IntegerField()
    breed = models.ForeignKey(
        "Breed",
        on_delete=models.PROTECT,
    )
    parent = models.OneToOneField(
        'Animal',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name='offspring',
    )

    def __str__(self):
        return self.nickname
