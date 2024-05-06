# views.py
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Airport
from .serializers import AirportSerializer
import pymongo
@api_view(['GET'])
def get_all_airports(request):
    
    connect_string = 'mongodb+srv://alexandrucarciumaru03:beyqsLvouvk3A3IG@database.ac3uoad.mongodb.net/' 
    my_client = pymongo.MongoClient(connect_string)
    dbname = my_client['your-Data']
    collection_name = dbname["Airports"]
    Airports = list(collection_name.find())
    serializer = AirportSerializer(Airports, many=True)
    return Response(serializer.data)
@api_view(['GET'])
def get_overcrowded_airports(request):
    
    connect_string = 'mongodb+srv://alexandrucarciumaru03:beyqsLvouvk3A3IG@database.ac3uoad.mongodb.net/' 
    my_client = pymongo.MongoClient(connect_string)
    dbname = my_client['your-Data']
    collection_name = dbname["Airports"]
    airport = Airport.objects.all()
    x = []
    for temp in airport:
        if temp.busyness == "overcrowded":
            x.append(temp)
    return Response(x)