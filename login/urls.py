
from django.urls import path
from .views import login,signup,get_all_users,remove_user,promote_user,demote_user

urlpatterns = [
    path('login', login, name='login'),
    path('signup', signup, name='signup'),
    path('get_all_users',get_all_users,name='get_all_users'),
    path('remove_user/', remove_user, name='remove_user'),
    path('promote_user/', promote_user, name='promote_user'),
    path('demote_user/', demote_user, name='demote_user'),
]
