from rest_framework import viewsets

# Create your views here.
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from .models import Entity, \
    ClientInformation, \
    DonorInformation, \
    VolunteerInformation
from .serializers import EntitySerializer, \
    ClientInformationSerializer, \
    DonorInformationSerializer, \
    VolunteerInformationSerializer, \
    CommunicationSerializer, \
    PhoneSerializer


class EntityViewSet(viewsets.ModelViewSet):
    queryset = Entity.objects.all()
    serializer_class = EntitySerializer

    @action(methods=['POST'])
    def phones(self, request, pk=None):
        entity = self.get_object()
        phone_serializer = PhoneSerializer(data=request.DATA)
        if phone_serializer.is_valid():
            entity.phones.add(phone_serializer.data)
            entity.save()
            entity_serializer = EntitySerializer(entity)
            return Response(entity_serializer.data)
        else:
            return Response(phone_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


class ClientInformationViewSet(viewsets.ModelViewSet):
    queryset = ClientInformation.objects.all()
    serializer_class = ClientInformationSerializer


class DonorInformationViewSet(viewsets.ModelViewSet):
    queryset = DonorInformation.objects.all()
    serializer_class = DonorInformationSerializer


class VolunteerInformationViewSet(viewsets.ModelViewSet):
    queryset = VolunteerInformation.objects.all()
    serializer_class = VolunteerInformationSerializer