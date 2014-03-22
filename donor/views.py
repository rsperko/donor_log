from django.shortcuts import render
from donor.models import DonorInformation
from rest_framework import viewsets
from donor.serializers import DonorInformationSerializer

# ViewSets define the view behavior.
# class DonorViewSet(viewsets.ModelViewSet):
#     model = Donor



# Create your views here.
class DonorInformationViewSet(viewsets.ModelViewSet):
    queryset = DonorInformation.objects.all()
    serializer_class = DonorInformationSerializer