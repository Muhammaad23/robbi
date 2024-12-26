from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    address = models.CharField(max_length=300)
    phone = models.CharField(max_length=20)
    opening_hours = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()


    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='menu_items')
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='menu_items')
    image = models.ImageField(upload_to='restaurant_images/', blank=True, null=True)

    def __str__(self):
        return self.name
