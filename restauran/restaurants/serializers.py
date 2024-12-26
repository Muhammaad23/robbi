from rest_framework import serializers
from .models import Restaurant, Category, MenuItem

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class MenuItemSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    restaurant = RestaurantSerializer(read_only=True)

    class Meta:
        model = MenuItem
        fields = '__all__'
