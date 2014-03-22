
from rest_framework import serializers

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

class DonorInformationSerializer(serializers.ModelSerializer):
    donations = DonationSerializer(many=True)

    class Meta:
        model = DonorInformation
        fields = (
            'id',
            'category',
            'type',
            'donations',
        )