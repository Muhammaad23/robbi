from django.urls import path
from .views import ClinicListView, ClinicDetailView

urlpatterns = [
    path('clinics/', ClinicListView.as_view(), name='clinic-list'),
    path('clinics/<int:pk>/', ClinicDetailView.as_view(), name='clinic-detail'),
]
