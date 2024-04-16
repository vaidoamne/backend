from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from login.models import UserProfile
from django.db import DatabaseError
from django.core.exceptions import ValidationError
from .serializers import UserSerializer
from django.contrib.auth.hashers import check_password
import pymongo
from django.conf import settings
@api_view(['POST'])
def login(request):
        email = request.data.get('email')
        password = request.data.get('password')

        if not email or not password:
            return Response({"error": "Email and password are required."}, status=status.HTTP_400_BAD_REQUEST)
        user = UserProfile.objects.all()
        for usera in user:
             print(usera.email)
             if usera.email == email and usera.password == password:
                return Response({
                    "first_name": usera.first_name,
                    "access_level": usera.level
                })

@api_view(['POST'])
def signup(request):
    try:
        connect_string = 'localhost:27017' 
        data = request.data
        my_client = pymongo.MongoClient(connect_string)
        dbname = my_client['your-Data']
        collection_name = dbname["users"]
        user_data = {
            "email": data.get("email", ""),
            "phone_number": data.get("phone_number", ""),
            "first_name": data.get("first_name", ""),
            "last_name": data.get("last_name", ""),
            "password": data.get("password", ""),
            "level": data.get("level", "")
        }
        collection_name.insert_one(user_data)
        
        return Response("User created successfully")
    
    except Exception as e:
        error_message = "An unexpected error occurred."
        return Response(error_message, status=500)  # Internal Server Error
