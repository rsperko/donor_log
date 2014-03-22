from django.shortcuts import render

# Create your views here.
from entity.models import Entity
from rest_framework import viewsets
from entity.serializers import EntitySerializer

# ViewSets define the view behavior.
# class DonorViewSet(viewsets.ModelViewSet):
#     model = Donor



# Create your views here.
class EntityViewSet(viewsets.ModelViewSet):
    queryset = Entity.objects.all()
    serializer_class = EntitySerializer