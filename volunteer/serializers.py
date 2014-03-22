
from rest_framework import serializers

from volunteer.models import *


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = (
            'id',
            'type',
            'notes',
        )


class AvailableHoursSerializer(serializers.ModelSerializer):
    class Meta:
        model = AvailableHours
        fields = (
            'start_time',
            'end_time',
        )


class AvailabilitySerializer(serializers.ModelSerializer):
    sunday = AvailableHoursSerializer()
    monday = AvailableHoursSerializer()
    tuesday = AvailableHoursSerializer()
    wednesday = AvailableHoursSerializer()
    thursday = AvailableHoursSerializer()
    friday = AvailableHoursSerializer()
    saturday = AvailableHoursSerializer()
    class Meta:
        model = Availability
        fields = (
        )


class VolunteerInformationSerializer(serializers.ModelSerializer):
    skills = SkillSerializer(many=True)
    availability = AvailabilitySerializer(many=True)

    class Meta:
        model = VolunteerInformation
        fields = (
            'id',
            'active',
        )