from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Clinic
from .serializers import ClinicSerializer
from django.db.models import Q


# List all clinics with optional filters
class ClinicListView(ListAPIView):
    serializer_class = ClinicSerializer

    def get_queryset(self):
        queryset = Clinic.objects.all()
        is_open_now = self.request.query_params.get('is_open_now', None)
        has_emergency_service = self.request.query_params.get('has_emergency_service', None)
        rating = self.request.query_params.get('rating', None)

        if is_open_now is not None:
            queryset = queryset.filter(is_open_now=is_open_now.lower() == 'true')
        if has_emergency_service is not None:
            queryset = queryset.filter(has_emergency_service=has_emergency_service.lower() == 'true')
        if rating:
            queryset = queryset.filter(rating__iexact=rating)

        return queryset


# Retrieve clinic details
class ClinicDetailView(RetrieveAPIView):
    queryset = Clinic.objects.all()
    serializer_class = ClinicSerializer
