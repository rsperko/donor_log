from django.shortcuts import render

# Create your views here.
from client.models import ClientInformation
from rest_framework import viewsets
from client.serializers import ClientInformationSerializer

# ViewSets define the view behavior.
# class DonorViewSet(viewsets.ModelViewSet):
#     model = Donor



# Create your views here.
class ClientInformationViewSet(viewsets.ModelViewSet):
    queryset = ClientInformation.objects.all()
    serializer_class = ClientInformationSerializer