from django.shortcuts import render

# Create your views here.
from volunteer.models import VolunteerInformation
from rest_framework import viewsets
from volunteer.serializers import VolunteerInformationSerializer

# ViewSets define the view behavior.
# class DonorViewSet(viewsets.ModelViewSet):
#     model = Donor



# Create your views here.
class VolunteerInformationViewSet(viewsets.ModelViewSet):
    queryset = VolunteerInformation.objects.all()
    serializer_class = VolunteerInformationSerializer