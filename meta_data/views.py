from django.shortcuts import render
from rest_framework.response import Response

# Create your views here.
from meta_data.models import META_DATA
from rest_framework import views

class MetaDataViewSet(views.APIView):
    def get(self, request):
        return Response(META_DATA)
