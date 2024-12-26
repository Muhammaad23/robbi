from django.urls import path
from .views import HotelListCreateView, HotelDetailView

urlpatterns = [
    path('hotels/', HotelListCreateView.as_view(), name='hotel-list-create'),
    path('hotels/<int:pk>/', HotelDetailView.as_view(), name='hotel-detail'),
]
