# Generated by Django 4.0.5 on 2022-06-16 14:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0005_title_remove_band_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='title',
            name='description',
            field=models.CharField(default='', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='title',
            name='sold',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='title',
            name='type',
            field=models.CharField(choices=[('Records', 'Disques'), ('Clothing', 'Vetements'), ('Posters', 'Affiches'), ('Miscellaneous', 'Divers')], default='Miscellaneous', max_length=20),
        ),
        migrations.AddField(
            model_name='title',
            name='year',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1945), django.core.validators.MaxValueValidator(1990)]),
        ),
    ]