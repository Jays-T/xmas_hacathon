from django.urls import path
from . import views

urlpatterns = [
    path('show_recipe/<int:recipe_id>', views.show_recipe, name='show_recipe')
]
