from rest_framework import serializers
from .models import Mosque, PrayerTime, NearbyService

class PrayerTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrayerTime
        fields = ['prayer_name', 'time']

class NearbyServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = NearbyService
        fields = ['name', 'address', 'latitude', 'longitude']

class MosqueSerializer(serializers.ModelSerializer):
    prayer_times = PrayerTimeSerializer(many=True, read_only=True)
    nearby_services = NearbyServiceSerializer(many=True, read_only=True)

    class Meta:
        model = Mosque
        fields = ['id', 'name', 'address', 'opening_hours', 'latitude', 'longitude',
                  'contact_number', 'description', 'prayer_times', 'nearby_services']
