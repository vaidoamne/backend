from rest_framework import serializers
from .models import Airport

class AirportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airport
        fields = [
            'airport_name',
            'country',
            'city',
            'airportX',
            'airportY',
            'airport_age',
            'flights_inbound',
            'flights_outbound',
            'delays_at_arrival',
            'delays_at_departure',
            'busyness',
            'airplane_capacity'
        ]
        db_table = "Airports"
