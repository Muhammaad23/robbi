from django.db import models

class Park(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='parks/images/', blank=True, null=True)
    description = models.TextField()
    working_hours = models.CharField(max_length=100)
    address = models.CharField(max_length=300)
    phone = models.CharField(max_length=15)
    location = models.CharField(max_length=200)  # You could use a geolocation library for lat/lng
    is_open_now = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Attraction(models.Model):
    park = models.ForeignKey(Park, related_name='attractions', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='parks_images/', blank=True, null=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    age_group = models.CharField(max_length=100)  # For example: "Adults", "Kids", etc.

    def __str__(self):
        return self.name
