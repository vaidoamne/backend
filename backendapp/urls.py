# urls.py
from django.urls import path
from .views import get_all_flights

urlpatterns = [
    path('flights', get_all_flights, name='flight-list'),
]
