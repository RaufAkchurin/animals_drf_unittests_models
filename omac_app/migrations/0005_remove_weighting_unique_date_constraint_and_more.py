# Generated by Django 4.2.3 on 2023-07-23 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('omac_app', '0004_weighting_weighting_unique_date_constraint'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='weighting',
            name='unique_date_constraint',
        ),
        migrations.AddConstraint(
            model_name='weighting',
            constraint=models.UniqueConstraint(fields=('animal', 'date'), name='unique_animal_weight_per_day'),
        ),
    ]
