from django.contrib import admin
from .models import Recipe


class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        'date',
        'title',
        'description',
        'author',
        'url',
        'ingredients',
        'method',
    )

admin.site.register(Recipe, RecipeAdmin)
