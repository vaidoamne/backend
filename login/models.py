# login/models.py
from django.db import models

class UserProfile(models.Model):
    email = models.EmailField(unique=True,primary_key=True)
    phone_number = models.CharField(max_length=20)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    LEVEL_CHOICES = [
        ('admin', 'Admin'),
        ('worker', 'Worker'),
        ('visitor', 'Visitor'),
    ]
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES)

    class Meta:
        managed = False
        db_table = 'userprofiles'
