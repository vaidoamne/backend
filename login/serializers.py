from rest_framework import serializers
from .models import UserProfile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['email', 'phone_number', 'first_name', 'last_name', 'password', 'level']
        db_table = "users" 