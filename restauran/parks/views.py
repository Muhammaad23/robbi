from rest_framework import generics
from .models import Park, Attraction
from .serializers import ParkSerializer, AttractionSerializer

class ParkListView(generics.ListAPIView):
    queryset = Park.objects.all()
    serializer_class = ParkSerializer

class ParkDetailView(generics.RetrieveAPIView):
    queryset = Park.objects.all()
    serializer_class = ParkSerializer

class AttractionListView(generics.ListAPIView):
    queryset = Attraction.objects.all()
    serializer_class = AttractionSerializer

class AttractionDetailView(generics.RetrieveAPIView):
    queryset = Attraction.objects.all()
    serializer_class = AttractionSerializer
