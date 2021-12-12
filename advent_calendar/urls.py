from django.urls import path
from . import views

urlpatterns = [
    path('', views.advent, name='calendar'),
    path('create-calendar/', views.create_advent, name='create_calendar'),
]
