
from rest_framework import serializers

from client.models import *

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = (
            'id',
            'date',
            'type',
            'notes',
        )

class ClientInformationSerializer(serializers.ModelSerializer):
    services = ServiceSerializer(many=True)

    class Meta:
        model = ClientInformation
        fields = (
            'id',
            'type',
        )