
from django.urls import path
from .views import get_all_airports,get_overcrowded_airports

urlpatterns = [
    path('get_all_airports', get_all_airports, name='get_all_airports'),
    path('get_overcrowded_airports', get_overcrowded_airports, name='get_overcrowded_airports'),
]
