from django.contrib.auth.models import User
from django.shortcuts import render
from requests import Response
from rest_framework import generics, permissions
from rest_framework.decorators import api_view

from api.models import Storage
from api.serializers import StorageSerializer


# Create your views here.
class StorageListView(generics.ListAPIView):
    queryset = Storage.objects.all()
    serializer_class = StorageSerializer
    permission_classes = (permissions.IsAuthenticated,)


@api_view(['POST'])
def create_slave_profile(request):
    email = request.POST.get['email']
    password = request.POST.get['password']
    profile = request.user.profile
    profile.image = None
    user = User(email=email, password=password, profile=profile).save()
    return Response(user)


@api_view(['GET'])
def get_all_slaves_profile(request):
    user = request.user
    group_id = user.profile.group_id
    slaves = User.objects.filter(profile__group=group_id)
    return slaves
