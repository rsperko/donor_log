
from rest_framework import serializers

from entity.models import *
from donor.models import *

class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phone
        fields = (
            'id',
            'preferred',
            'number',
            'type',
        )

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = (
            'id',
            'preferred',
            'care_of',
            'line1',
            'line2',
            'city',
            'state',
            'postalCode',
        )

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = (
            'id',
            'date_time',
            'type',
            'notes',
        )

class EntitySerializer(serializers.ModelSerializer):
    phones = PhoneSerializer(many=True)
    addresses = AddressSerializer(many=True)

    class Meta:
        model = Entity
        fields = (
            'id',
            'added',
            'email',
            'notes',
            'phones',
            'addresses',
        )