from django.db import models

class Mosque(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    opening_hours = models.CharField(max_length=50)  # Example: "09:00 - 23:00"
    latitude = models.FloatField()
    longitude = models.FloatField()
    contact_number = models.CharField(max_length=20, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class PrayerTime(models.Model):
    mosque = models.ForeignKey(Mosque, on_delete=models.CASCADE, related_name="prayer_times")
    prayer_name = models.CharField(max_length=50)  # E.g., "Fajr", "Dhuhr"
    time = models.TimeField()

    def __str__(self):
        return f"{self.prayer_name} - {self.mosque.name}"

class NearbyService(models.Model):
    mosque = models.ForeignKey(Mosque, on_delete=models.CASCADE, related_name="nearby_services")
    name = models.CharField(max_length=255)
    address = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name
