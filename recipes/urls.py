from django.urls import path
from . import views

urlpatterns = [
    path('show_recipes/', views.show_recipes, name='show_recipes')
]
