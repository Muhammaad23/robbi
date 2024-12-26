from django.contrib import admin
from .models import Mosque, PrayerTime, NearbyService

# PrayerTime Inline for Mosque Admin
class PrayerTimeInline(admin.TabularInline):  # TabularInline shows data in a table format
    model = PrayerTime
    extra = 1  # Number of empty forms to display for adding new entries
    fields = ('prayer_name', 'time')  # Fields to display in the inline form
    verbose_name = "Prayer Time"
    verbose_name_plural = "Prayer Times"

# NearbyService Inline for Mosque Admin
class NearbyServiceInline(admin.TabularInline):
    model = NearbyService
    extra = 1
    fields = ('name', 'address', 'latitude', 'longitude')
    verbose_name = "Nearby Service"
    verbose_name_plural = "Nearby Services"

# Mosque Admin
@admin.register(Mosque)
class MosqueAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'opening_hours', 'contact_number')  # Columns in the admin list view
    search_fields = ('name', 'address')  # Searchable fields
    list_filter = ('opening_hours',)  # Filter by opening hours
    inlines = [PrayerTimeInline, NearbyServiceInline]  # Include PrayerTime and NearbyService inline forms

# PrayerTime Admin
@admin.register(PrayerTime)
class PrayerTimeAdmin(admin.ModelAdmin):
    list_display = ('mosque', 'prayer_name', 'time')  # Columns in the admin list view
    search_fields = ('mosque__name', 'prayer_name')  # Searchable fields (related field using double underscores)
    list_filter = ('prayer_name',)  # Filter by prayer name

# NearbyService Admin
@admin.register(NearbyService)
class NearbyServiceAdmin(admin.ModelAdmin):
    list_display = ('mosque', 'name', 'address')  # Columns in the admin list view
    search_fields = ('mosque__name', 'name', 'address')  # Searchable fields
    list_filter = ('mosque',)  # Filter by mosque
