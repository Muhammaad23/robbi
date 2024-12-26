from django.urls import path
from .views import RestaurantViewSet, CategoryViewSet, MenuItemViewSet

urlpatterns = [
    # Restaurant Endpoints
    path('restaurants/', RestaurantViewSet.as_view({'get': 'list', 'post': 'create'}), name='restaurant-list'),
    path('restaurants/<int:pk>/', RestaurantViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='restaurant-detail'),

    # Category Endpoints
    path('categories/', CategoryViewSet.as_view({'get': 'list', 'post': 'create'}), name='category-list'),
    path('categories/<int:pk>/', CategoryViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='category-detail'),

    # Menu Item Endpoints
    path('menu-items/', MenuItemViewSet.as_view({'get': 'list', 'post': 'create'}), name='menu-item-list'),
    path('menu-items/<int:pk>/', MenuItemViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='menu-item-detail'),
]
