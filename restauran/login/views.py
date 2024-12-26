from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from .serializers import EmailLoginSerializer

User = get_user_model()

class EmailLoginView(APIView):
    def post(self, request):
        serializer = EmailLoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            user = User.objects.get(email=email)

            # Create JWT tokens
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)

            # Send login email
            send_mail(
                subject="Your Login Link",
                message=f"Here is your access token: {access_token}\nUse the refresh token to renew access.",
                from_email="your-email@example.com",
                recipient_list=[email],
            )

            return Response({"message": "Login link sent successfully."}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
