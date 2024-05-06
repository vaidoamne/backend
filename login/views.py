# Django views.py

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from login.models import UserProfile
from django.db import DatabaseError
from django.core.exceptions import ValidationError
from .serializers import UserSerializer
import pymongo
from django.conf import settings
from rest_framework.exceptions import AuthenticationFailed
@api_view(['POST'])
def login(request):
        email = request.data.get('email')
        password = request.data.get('password')

        if not email or not password:
            return Response({"error": "Email and password are required."}, status=status.HTTP_400_BAD_REQUEST)
        user = UserProfile.objects.all()
        for usera in user:
             print(usera.email)
             print(usera.password)
             if usera.email == email and usera.password == password:
                return Response({
                    "first_name": usera.first_name,
                    "access_level": usera.level
                })
             

@api_view(['POST'])
def signup(request):
    try:
        data = request.data
        connect_string = 'mongodb+srv://alexandrucarciumaru03:beyqsLvouvk3A3IG@database.ac3uoad.mongodb.net/' 
        my_client = pymongo.MongoClient(connect_string)
        dbname = my_client['your-Data']
        collection_name = dbname["userprofiles"]
        user_data = {
            "email": data.get("email"),
            "phone_number": data.get("phone_number"),
            "first_name": data.get("first_name"),
            "last_name": data.get("last_name"),
            "password": data.get("password"),
            "level": data.get("level")
        }
        collection_name.insert_one(user_data)
        
        return Response("User created successfully", status=status.HTTP_201_CREATED)
    
    except pymongo.errors.PyMongoError as e:
        return Response("An unexpected error occurred with MongoDB", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        return Response("An unexpected error occurred" , status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@api_view(['GET'])
def get_all_users(request):
    
    connect_string = 'mongodb+srv://alexandrucarciumaru03:beyqsLvouvk3A3IG@database.ac3uoad.mongodb.net/' 
    my_client = pymongo.MongoClient(connect_string)
    dbname = my_client['your-Data']
    collection_name = dbname["userprofiles"]
    users = list(collection_name.find())
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def remove_user(request):
    email = request.data.get('email')
    # Connect to MongoDB
    connect_string = 'mongodb+srv://alexandrucarciumaru03:beyqsLvouvk3A3IG@database.ac3uoad.mongodb.net/'
    my_client = pymongo.MongoClient(connect_string)
    dbname = my_client['your-Data']
    collection_name = dbname["userprofiles"]
    
    result = collection_name.delete_one({"email": email})
    
    if result.deleted_count == 1:
        return Response({"message": "User removed successfully"}, status=status.HTTP_204_NO_CONTENT)
    else:
        return Response({"message": "User not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def promote_user(request):
    email = request.data.get('email')
    # Connect to MongoDB
    connect_string = 'mongodb+srv://alexandrucarciumaru03:beyqsLvouvk3A3IG@database.ac3uoad.mongodb.net/' 
    my_client = pymongo.MongoClient(connect_string)
    dbname = my_client['your-Data']
    collection_name = dbname["userprofiles"]
    
    # Update user's level to admin
    result = collection_name.update_one({"email": email}, {"$set": {"level": "admin"}})
    
    if result.modified_count == 1:
        return Response({"message": "User promoted to admin"}, status=status.HTTP_200_OK)
    else:
        return Response({"message": "User not found"}, status=status.HTTP_404_NOT_FOUND)



@api_view(['POST'])
def demote_user(request):
    email = request.data.get('email')
    # Connect to MongoDB
    connect_string = 'mongodb+srv://alexandrucarciumaru03:beyqsLvouvk3A3IG@database.ac3uoad.mongodb.net/' 
    my_client = pymongo.MongoClient(connect_string)
    dbname = my_client['your-Data']
    collection_name = dbname["userprofiles"]
    
    # Update user's level to worker
    result = collection_name.update_one({"email": email}, {"$set": {"level": "worker"}})
    
    if result.modified_count == 1:
        return Response({"message": "User demoted to worker"}, status=status.HTTP_200_OK)
    else:
        return Response({"message": "User not found"}, status=status.HTTP_404_NOT_FOUND)

