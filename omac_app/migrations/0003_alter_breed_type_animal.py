# Generated by Django 4.2.3 on 2023-07-22 16:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('omac_app', '0002_rename_anymaltype_animaltype_breed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='breed',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='omac_app.animaltype'),
        ),
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(unique=True)),
                ('sex', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('nickname', models.CharField(max_length=50)),
                ('arrival_date', models.DateField()),
                ('arrival_age', models.IntegerField()),
                ('breed', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='omac_app.breed')),
                ('parent', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='offspring', to='omac_app.animal')),
            ],
        ),
    ]
