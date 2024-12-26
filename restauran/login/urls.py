from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import EmailLoginView

urlpatterns = [
    path('login/', EmailLoginView.as_view(), name='email-login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
]
