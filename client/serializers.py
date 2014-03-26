
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


class FamilyMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = FamilyMember
        fields = (
            'type',
            'name',
            'birth_date',
        )


class ClientInformationSerializer(serializers.ModelSerializer):
    services = ServiceSerializer(many=True)
    family_members = FamilyMemberSerializer(many=True)

    class Meta:
        model = ClientInformation
        fields = (
            'id',
            'type',
            'family_members',
            'services',
        )