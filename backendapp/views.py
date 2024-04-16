# views.py
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Flight
from .serializers import FlightSerializer
import pymongo
@api_view(['GET'])
def get_all_flights(request):
    
    connect_string = 'localhost:27017' 
    my_client = pymongo.MongoClient(connect_string)
    dbname = my_client['your-Data']
    collection_name = dbname["backendapp_flight"]
    print("stage 1")
    flights = list(collection_name.find())
    print(flights)
    print("stage 2")
    serializer = FlightSerializer(flights, many=True)
        
    print("stage 3")
    return Response(serializer.data)