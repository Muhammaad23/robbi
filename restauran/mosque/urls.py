from django.urls import path
from .views import MosqueListCreateView, MosqueRetrieveUpdateDeleteView

urlpatterns = [
    path('mosque/', MosqueListCreateView.as_view(), name='mosque-list-create'),
    path('mosque/<int:pk>/', MosqueRetrieveUpdateDeleteView.as_view(), name='mosque-detail'),
]
