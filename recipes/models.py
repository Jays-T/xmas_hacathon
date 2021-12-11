from django.contrib.postgres.fields import ArrayField
from django.db import models


class Recipe(models.Model):
    date = models.DateField(null=True, blank=True)
    title = models.CharField(max_length=255, null=False, blank=False)
    description = models.CharField(max_length=500, null=True, blank=True)
    author = models.CharField(max_length=255, null=True, blank=True)
    url = models.URLField(max_length=1024, null=True, blank=True)
    ingredients = ArrayField(models.CharField(max_length=200), blank=True, null=True)
    method = ArrayField(models.CharField(max_length=200), blank=True, null=True)

    def __str__(self):
        return self.title
