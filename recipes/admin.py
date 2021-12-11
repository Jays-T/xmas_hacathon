from django.contrib import admin
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin
from .models import Recipe


class RecipeAdmin(admin.ModelAdmin, DynamicArrayMixin):
    list_display = (
        'title',
        'description',
        'author',
        'url',
        'ingredients',
        'method',
    )

admin.site.register(Recipe, RecipeAdmin)
