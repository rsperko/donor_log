from rest_framework import serializers

from .models import Entity, Phone, Address, Communication, \
    ClientInformation, FamilyMember, Service, \
    DonorInformation, Donation, \
    VolunteerInformation, Skill


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


class CommunicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Communication
        # fields = (
        #     'id',
        #     'date',
        #     'type',
        #     'notes',
        #     'connected',
        #     # 'entity_id',
        # )


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
    services = ServiceSerializer(many=True, allow_add_remove=True)
    family_members = FamilyMemberSerializer(many=True, allow_add_remove=True)

    class Meta:
        model = ClientInformation
        fields = (
            'id',
            'type',
            'family_members',
            'services',
        )


class DonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donation
        fields = (
            'id',
            'date',
            'monetary_amount',
            'type',
            'notes',
        )


class DonorInformationSerializer(serializers.ModelSerializer):
    donations = DonationSerializer(many=True, allow_add_remove=True)

    class Meta:
        model = DonorInformation
        fields = (
            'id',
            'category',
            'type',
            'donations',
        )


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = (
            'id',
            'type',
            'notes',
        )


class VolunteerInformationSerializer(serializers.ModelSerializer):
    skills = SkillSerializer(many=True, allow_add_remove=True)

    class Meta:
        model = VolunteerInformation
        fields = (
            'id',
            'active',
            'skills',
        )


class EntitySerializer(serializers.ModelSerializer):
    phones = PhoneSerializer(many=True, allow_add_remove=True)
    addresses = AddressSerializer(many=True, allow_add_remove=True)
    communications = CommunicationSerializer(many=True, allow_add_remove=True)
    # donor_information = DonorInformationSerializer()
    # client_information = ClientInformationSerializer()
    # volunteer_information = VolunteerInformationSerializer()

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
            'communications',
            # 'donor_information',
            # 'client_information',
            # 'volunteer_information',
        )
