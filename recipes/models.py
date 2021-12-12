from django_better_admin_arrayfield.models.fields import ArrayField
from django.db import models


class Recipe(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    description = models.CharField(max_length=500, null=True, blank=True)
    author = models.CharField(max_length=255, null=True, blank=True)
    url = models.URLField(max_length=1024, null=True, blank=True)
    ingredients = ArrayField(models.CharField(max_length=200, blank=True))  # noqa: E501
    method = ArrayField(models.CharField(max_length=200, blank=True))  # noqa: E501

    def __str__(self):
        return self.title
