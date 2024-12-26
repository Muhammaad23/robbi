from django.db import models

class Clinic(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    phone_number = models.CharField(max_length=20)
    working_hours = models.CharField(max_length=50)
    is_open_now = models.BooleanField(default=False)
    has_emergency_service = models.BooleanField(default=False)
    rating = models.CharField(max_length=50)  # Gold/Silver/Standard
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name
