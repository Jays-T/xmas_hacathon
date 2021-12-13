from django.urls import path
from . import views

urlpatterns = [
    path('', views.advent, name='calendar'),
    path('create-calendar/', views.create_advent, name='create_calendar'),
    path('naughty/', views.naughty, name='naughty'),
    path('mark-complete/<int:day_id>/<calendar_id>', views.set_day_recipe_complete, name='mark_complete')  # noqa: E501
]
