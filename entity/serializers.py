
from rest_framework import serializers

from entity.models import Entity, Phone, Address, Contact
from donor.serializers import DonorInformationSerializer
from client.serializers import ClientInformationSerializer
from volunteer.serializers import VolunteerInformationSerializer


class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phone
        fields = (
            'id',
            'primary',
            'number',
            'type',
        )


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = (
            'id',
            'primary',
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
    contacts = ContactSerializer(many=True)
    donor_information = DonorInformationSerializer()
    client_information = ClientInformationSerializer()
    volunteer_information = VolunteerInformationSerializer()

    class Meta:
        model = Entity
        fields = (
            'id',
            'added',
            'first_name',
            'last_name',
            'institution_name',
            'email',
            'notes',
            'phones',
            'addresses',
            'donor_information',
            'client_information',
        )