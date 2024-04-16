from django.db import models


class Flight(models.Model):
        id = models.CharField(max_length=100)
        flight_number = models.CharField(max_length=20,primary_key=True)  # Assuming flight numbers can include characters
        timestamp = models.DateTimeField()
        destination = models.CharField(max_length=200)
        altitude = models.IntegerField()
        airspeed = models.IntegerField()
        temperature = models.IntegerField()
        pressure = models.IntegerField()
        passengers = models.IntegerField()
        capacity = models.IntegerField()
        

        class Meta:
                managed = False
                db_table = 'backendapp_flight'
        