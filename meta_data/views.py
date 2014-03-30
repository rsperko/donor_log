from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

# Create your views here.
from meta_data.models import META_DATA
from rest_framework import views


class MetaDataViewSet(views.APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        return Response(META_DATA)
