from rest_framework import serializers
from weather_app.models import Weather


class WeatherSerializer(serializers.ModelSerializer):
    """
    Weather serializer
    """
    class Meta:
        model = Weather
        fields = '__all__'
