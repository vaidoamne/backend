"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from backendapp.views import get_all_flights
from login.views import login,signup,get_all_users,remove_user,promote_user,demote_user
from airports.views import get_all_airports,get_overcrowded_airports
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('flights', get_all_flights),
    path('login', login),
    path('signup', signup),
    path('remove_user/', remove_user, name='remove_user'),
    path('promote_user/', promote_user, name='promote_user'),
    path('demote_user/', demote_user, name='demote_user'),
    path('get_all_airports', get_all_airports, name='get_all_airports'),
    path('get_overcrowded_airports', get_overcrowded_airports, name='get_overcrowded_airports'),
    path('get_all_users', get_all_users, name='get_all_users'),
]
