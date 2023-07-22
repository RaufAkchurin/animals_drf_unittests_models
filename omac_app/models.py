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

# «Animal» содержит данные о животных –
# инвентарный номер,
# пол,
# кличка,
# дата прибытия,
# возраст прибытия (в месяцах),
# данные о породе животного,
# данные об одном родителе(ссылка на другой экземпляр животного).
#
# Инвентарный номер не может повторяться.
# «Weighting» содержит данные о взвешивании животного – животное, дата, вес в кг.
# При условии, что у одного экземпляра животного не может быть 2 взвешивания в 1 дату.
