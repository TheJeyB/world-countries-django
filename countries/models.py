from django.db import models

# Create your models here.

class Country(models.Model):
    cca3 = models.CharField(max_length=3, unique=True)  # clé unique
    name = models.CharField(max_length=200)
    cca2 = models.CharField(max_length=2)
    capital = models.CharField(max_length=200, null=True, blank=True)
    region = models.CharField(max_length=100, null=True, blank=True)
    subregion = models.CharField(max_length=100, null=True, blank=True)
    population = models.BigIntegerField(null=True, blank=True)
    area = models.FloatField(null=True, blank=True)
    flag = models.URLField(null=True, blank=True)
    currencies = models.JSONField(null=True, blank=True)  # dictionnaire JSON

    def __str__(self):
        return self.name