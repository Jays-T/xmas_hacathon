from django.urls import path
from . import views

urlpatterns = [
    path('', views.advent, name='calendar'),
]
