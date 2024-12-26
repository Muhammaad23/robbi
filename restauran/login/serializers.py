from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()

class EmailLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_email(self, email):
        if not User.objects.filter(email=email).exists():
            raise serializers.ValidationError("No user found with this email.")
        return email
