from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Band(models.Model):
    class Genre(models.TextChoices):
        HIP_HOP = 'HH'
        SYNTH_POP = 'SH'
        ALTERNATIVE_ROCK = 'AR'
    name = models.fields.CharField(max_length=100)
    genre =models.fields.CharField(choices=Genre.choices, max_length=5)
    biography = models.fields.CharField(max_length=1000)
    year_formed = models.fields.IntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(2022)]
    )
    active = models.fields.BooleanField(default=True)
    official_page = models.fields.URLField(null=True, blank=True)

    def __str__(self):
        return f'{self.name}'


class Title(models.Model):
    class Type(models.TextChoices):
        DISQUES = 'Records'
        VETEMENT = 'Clothing'
        AFFICHE = 'Posters'
        DIVERS = 'Miscellaneous'

    title = models.fields.CharField(max_length=100)
    description = models.fields.CharField(max_length=500)
    sold = models.fields.BooleanField(default=False)
    year = models.fields.IntegerField(validators=[MinValueValidator(1945), MaxValueValidator(1990)],
                                      null=True,
                                      blank=True)
    type = models.fields.CharField(choices=Type.choices, default='Miscellaneous', max_length=20)
    band = models.ForeignKey(Band, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.title}'


