from django.contrib import admin
from .models import Park, Attraction

class AttractionInline(admin.TabularInline):  # To display attractions inline in the Park admin
    model = Attraction
    extra = 1  # Number of empty forms to show for adding new attractions

@admin.register(Park)
class ParkAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone', 'is_open_now')  # Fields to display in the admin list view
    list_filter = ('is_open_now',)  # Filter sidebar for 'is_open_now'
    search_fields = ('name', 'address')  # Search by name and address
    inlines = [AttractionInline]  # Inline attractions in the park admin page
    prepopulated_fields = {"location": ("name",)}  # Example: autopopulate location slug from name (if applicable)

@admin.register(Attraction)
class AttractionAdmin(admin.ModelAdmin):
    list_display = ('name', 'park', 'price', 'age_group')  # Fields to display in the admin list view
    list_filter = ('age_group', 'park')  # Filter sidebar for age group and park
    search_fields = ('name',)  # Search by attraction name
