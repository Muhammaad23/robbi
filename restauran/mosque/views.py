from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Mosque
from .serializers import MosqueSerializer

class MosqueListCreateView(generics.ListCreateAPIView):
    queryset = Mosque.objects.all()
    serializer_class = MosqueSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['name']  # Example: Filter by name
    search_fields = ['name', 'address']  # Example: Search by name or address

class MosqueRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mosque.objects.all()
    serializer_class = MosqueSerializer
