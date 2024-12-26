# admin.py
from django.contrib import admin
from .models import Restaurant, Category, MenuItem

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone', 'opening_hours')
    search_fields = ('name', 'address')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'restaurant')
    list_filter = ('category', 'restaurant')
    search_fields = ('name',)
