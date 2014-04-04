from rest_framework import viewsets
from rest_framework import filters
import django_filters

# Create your views here.
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from .models import Entity, \
    ClientInformation, \
    DonorInformation, \
    VolunteerInformation, Communication
from .serializers import EntitySerializer, \
    ClientInformationSerializer, \
    DonorInformationSerializer, \
    VolunteerInformationSerializer, \
    CommunicationSerializer


class EntityFilter(django_filters.FilterSet):
    first_name = django_filters.CharFilter(name='first_name', lookup_type='icontains')
    last_name = django_filters.CharFilter(name='last_name', lookup_type='icontains')
    skills = django_filters.CharFilter(name='volunteer_information__skills__type', lookup_type='in')
    active = django_filters.BooleanFilter(name='volunteer_information__active', lookup_type='in')
    notes = django_filters.CharFilter(name='notes', lookup_type='icontains')

    class Meta:
        model = Entity
        fields = ['first_name', 'last_name', 'skills', 'active', 'notes']


class EntityViewSet(viewsets.ModelViewSet):
    queryset = Entity.objects.all()
    serializer_class = EntitySerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = EntityFilter

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

    def __delete_communication(self, request):
        comm_id = request.QUERY_PARAMS['comm_id']
        if comm_id:
            comm = Communication.objects.filter(id=comm_id)
            comm.delete()
            entity = self.get_object()
            entity_serializer = EntitySerializer(entity)
            return Response(entity_serializer.data)
        else:
            return Response({},
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
            return self.__delete_communication(request)
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
