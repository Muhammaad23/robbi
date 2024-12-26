from django.urls import path
from .views import ParkListView, ParkDetailView, AttractionListView, AttractionDetailView

urlpatterns = [
    path('parks/', ParkListView.as_view(), name='park-list'),
    path('parks/<int:pk>/', ParkDetailView.as_view(), name='park-detail'),
    path('attractions/', AttractionListView.as_view(), name='attraction-list'),
    path('attractions/<int:pk>/', AttractionDetailView.as_view(), name='attraction-detail'),
]
