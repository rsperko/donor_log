from django.shortcuts import render
from donor.models import Donor
from rest_framework import viewsets
from donor.serializers import DonorSerializer

# ViewSets define the view behavior.
# class DonorViewSet(viewsets.ModelViewSet):
#     model = Donor



# Create your views here.
class DonorViewSet(viewsets.ModelViewSet):
    queryset = Donor.objects.all()
    serializer_class = DonorSerializer