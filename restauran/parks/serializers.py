from rest_framework import serializers
from .models import Park, Attraction

class AttractionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attraction
        fields = '__all__'

class ParkSerializer(serializers.ModelSerializer):
    attractions = AttractionSerializer(many=True, read_only=True)

    class Meta:
        model = Park
        fields = '__all__'
