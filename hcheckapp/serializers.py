from rest_framework import serializers
from .models import ServiceHealthData

class ServiceHealthDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceHealthData
        fields = '__all__'
