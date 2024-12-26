from django.db import models

class Hotel(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="hotel_images/")
    rating = models.IntegerField(choices=[(i, f"{i} yulduzli") for i in range(2, 6)])
    is_open_now = models.BooleanField(default=True)
    working_hours = models.CharField(max_length=50)
    address = models.TextField()
    phone = models.CharField(max_length=20)
    description = models.TextField(blank=True, null=True)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name
