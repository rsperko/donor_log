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

    def __add_communication(self, comm_serializer):
        if comm_serializer.is_valid():
            entity = self.get_object()
            comm_serializer.object.entity_id = entity.id
            comm_serializer.save()
            entity_serializer = EntitySerializer(entity)
            return Response(entity_serializer.data)
        else:
            return Response(comm_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    def __delete_communication(self, comm_serializer):
        if comm_serializer.is_valid():
            comm_serializer.save()
            entity = self.get_object()
            entity_serializer = EntitySerializer(entity)
            return Response(entity_serializer.data)
        else:
            return Response(comm_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    def __update_communication(self, comm_serializer):
        if comm_serializer.is_valid():
            comm_serializer.delete()
            entity = self.get_object()
            entity_serializer = EntitySerializer(entity)
            return Response(entity_serializer.data)
        else:
            return Response(comm_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['POST', 'DELETE', 'PUT'])
    def communications(self, request, pk=None):
        comm_serializer = CommunicationSerializer(data=request.DATA)
        if request.method == 'POST':
            return self.__add_communication(comm_serializer)
        elif request.method == 'DELETE':
            return self.__delete_communication(comm_serializer)
        else:
            return self.__update_communication(comm_serializer)


class ClientInformationViewSet(viewsets.ModelViewSet):
    queryset = ClientInformation.objects.all()
    serializer_class = ClientInformationSerializer


class DonorInformationViewSet(viewsets.ModelViewSet):
    queryset = DonorInformation.objects.all()
    serializer_class = DonorInformationSerializer


class VolunteerInformationViewSet(viewsets.ModelViewSet):
    queryset = VolunteerInformation.objects.all()
    serializer_class = VolunteerInformationSerializer