# serializers.py
from rest_framework import serializers
from .models import Flight

class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = [
        'id',
        'flight_number',
        'timestamp',
        'destination',
        'altitude',
        'airspeed',
        'temperature',
        'pressure',
        'passengers',
        'capacity',
        'company_name',
        'plane_name',
        'plane_model',
        'plane_age',
        'current_occupied_spaces',
        'speed',
        'startX',
        'startY',
        'currentX',
        'currentY',
        'endX',
        'endY',
        'starting_airport_name',
        'starting_airport_X',
        'starting_airport_Y',
        'end_airport_name',
        'end_airport_X',
        'end_airport_Y',
        'departure_time',
        'estimated_arrival_time',
        'arrival_time'
        ]

        db_table = "backendapp_flight" 


