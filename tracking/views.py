from rest_framework import viewsets
from rest_framework import filters
import django_filters

# Create your views here.

from .models import Entity, \
    Communication, \
    Donation
from .serializers import EntitySerializer, \
    CommunicationSerializer, \
    DonationSerializer


class EntityFilter(django_filters.FilterSet):
    first_name = django_filters.CharFilter(name='first_name', lookup_type='icontains')
    last_name = django_filters.CharFilter(name='last_name', lookup_type='icontains')
    notes = django_filters.CharFilter(name='notes', lookup_type='icontains')

    volunteer_unset = django_filters.NumberFilter('volunteer_information__id', lookup_type='gt')
    skills = django_filters.CharFilter(name='volunteer_information__skills__type', lookup_type='in')
    volunteer_active = django_filters.BooleanFilter(name='volunteer_information__active', lookup_type='in')

    donor_unset = django_filters.NumberFilter('donor_information__id', lookup_type='gt')
    donation_types = django_filters.CharFilter(name='donor_information__donations__type', lookup_type='in')
    donor_type = django_filters.CharFilter(name='donor_information__type', lookup_type='in')
    donor_category = django_filters.CharFilter(name='donor_information__category', lookup_type='in')

    class Meta:
        model = Entity
        fields = ['first_name', 'last_name', 'notes',
                  'volunteer_unset', 'skills', 'volunteer_active',
                  'donor_unset', 'donation_types', 'donor_type', 'donor_category']


class EntityViewSet(viewsets.ModelViewSet):
    queryset = Entity.objects.all()
    serializer_class = EntitySerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = EntityFilter


class CommunicationViewSet(viewsets.ModelViewSet):
    queryset = Communication.objects.all()
    serializer_class = CommunicationSerializer


class DonationViewSet(viewsets.ModelViewSet):
    queryset = Donation.objects.all()
    serializer_class = DonationSerializer
