import datetime

from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.models import Storage
from api.serializers import StorageSerializer, RegisterSerializer, EditAccessLayerSerializer
from users.models import Profile


# Create your views here.
class StorageListView(generics.ListAPIView):
    queryset = Storage.objects.all()
    serializer_class = StorageSerializer
    permission_classes = (permissions.IsAuthenticated,)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def register_group_user(request):
    if request.user.profile.access_layer in [0, 1]:
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = User.objects.create_user(
                username=serializer.data.get('username'),
                email=serializer.data.get('email'),
                password=serializer.data.get('password'),
            )
            user.save()
            user.profile.access_layer = serializer.data.get('access_layer')
            user.save()

            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    else:
        return Response(status=401)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_info(request):
    date = datetime.date.today()
    user = request.user
    if user.group.tariff_exp <= date:
        user.group.tariff_level = 0
        user.group.tariff_exp = None
        user.group.volume = 0
        user.group.save()
        user.save()
        return Response({
            'error': 'tariff expired'
        })
    else:
        response = {
            'username': user.username,
            'access_layer': user.profile.access_layer,
            'group_id': user.group.id,
        }
        return Response(response)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_group_members(request):
    group = request.user.group
    members = group.members.order_by('profile__access_layer').all()
    response: [dict] = []
    for member in members:
        response.append(
            {
                'username': member.username,
                'access_layer': member.profile.access_layer,
            }
        )
    return Response(response)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def edit_access_layer(request):
    if request.user.profile.access_layer in [0, 1]:
        serializer = EditAccessLayerSerializer(
            data=request.data
        )
        if serializer.is_valid():
            data = request.user.group.members.filter(username=serializer.data.get('username')).first()
            data.profile.access_layer = serializer.data.get('access_layer')
            data.save()
            return Response(status=200)
        else:
            return Response(serializer.errors)
    else:
        return Response(status=401)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_user(request):
    if request.user.profile.access_layer in [0, 1]:
        username = request.GET.get('username')
        User.objects.filter(username=username).delete()
        return Response(status=201)
    else:
        return Response(status=401)
