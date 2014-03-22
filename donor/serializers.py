
from rest_framework import serializers

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

class DonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donation
        fields = (
            'id',
            'date',
            'monetary_amount',
            'in_kind',
            'type',
            'notes',
        )

class DonorContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = DonorContact
        fields = (
            'id',
            'date_time',
            'type',
            'notes',
        )

class DonorSerializer(serializers.ModelSerializer):
    phones = PhoneSerializer(many=True)
    addresses = AddressSerializer(many=True)
    donations = DonationSerializer(many=True)

    class Meta:
        model = Donor
        fields = (
            'id',
            'added',
            'first_name',
            'last_name',
            'institution_name',
            'category',
            'email',
            'notes',
            'type',
            'phones',
            'addresses',
            'donations',
        )