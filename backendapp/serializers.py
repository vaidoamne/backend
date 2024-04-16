# serializers.py
from rest_framework import serializers
from .models import Flight

class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = ['id','flight_number', 'timestamp', 'destination', 'altitude', 'airspeed', 'temperature', 'pressure', 'passengers','capacity']
        db_table = "backendapp_flight" 


