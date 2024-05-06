from django.db import models

class Airport(models.Model):
    airport_name = models.CharField(max_length=200)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    airportX = models.FloatField()
    airportY = models.FloatField()
    airport_age = models.IntegerField()
    flights_inbound = models.IntegerField()
    flights_outbound = models.IntegerField()
    delays_at_arrival = models.IntegerField()
    delays_at_departure = models.IntegerField()
    busyness = models.CharField(max_length=20)
    airplane_capacity = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Airports'
