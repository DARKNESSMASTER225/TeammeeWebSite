from django.shortcuts import render
from rest_framework import generics, permissions

from api.models import Storage
from api.serializers import StorageSerializer


# Create your views here.
class StorageListView(generics.ListAPIView):
    queryset = Storage.objects.all()
    serializer_class = StorageSerializer
    permission_classes = (permissions.IsAuthenticated,)





