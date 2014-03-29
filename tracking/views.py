from rest_framework import viewsets

# Create your views here.

from .models import Entity, \
    ClientInformation, \
    DonorInformation, \
    VolunteerInformation
from .serializers import EntitySerializer, \
    ClientInformationSerializer, DonorInformationSerializer, VolunteerInformationSerializer


class EntityViewSet(viewsets.ModelViewSet):
    queryset = Entity.objects.all()
    serializer_class = EntitySerializer


class ClientInformationViewSet(viewsets.ModelViewSet):
    queryset = ClientInformation.objects.all()
    serializer_class = ClientInformationSerializer


class DonorInformationViewSet(viewsets.ModelViewSet):
    queryset = DonorInformation.objects.all()
    serializer_class = DonorInformationSerializer


class VolunteerInformationViewSet(viewsets.ModelViewSet):
    queryset = VolunteerInformation.objects.all()
    serializer_class = VolunteerInformationSerializer