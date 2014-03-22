
from rest_framework import serializers

from entity.serializers import *
from donor.models import *

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

class DonorSerializer(EntitySerializer):
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