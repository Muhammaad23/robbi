from django.contrib import admin
from .models import Clinic

@admin.register(Clinic)
class ClinicAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'working_hours', 'is_open_now', 'latitude', 'longitude', 'rating')
    list_filter = ('rating', 'is_open_now', 'has_emergency_service')
    search_fields = ('name', 'address')
    ordering = ('name',)
    fieldsets = (
        (None, {
            'fields': ('name', 'address', 'phone_number', 'working_hours', 'rating')
        }),
        ('Status', {
            'fields': ('is_open_now', 'has_emergency_service')
        }),
        ('Location', {
            'fields': ('latitude', 'longitude')
        }),
    )
