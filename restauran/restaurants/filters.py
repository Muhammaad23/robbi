from django_filters import rest_framework as filters
from .models import MenuItem

class MenuItemFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = filters.NumberFilter(field_name='price', lookup_expr='lte')

    class Meta:
        model = MenuItem
        fields = ['category', 'restaurant', 'min_price', 'max_price']
