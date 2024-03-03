import datetime

import django
from django.contrib.auth.models import User
from django.db.models.expressions import NoneType
from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.models import Storage
from api.serializers import StorageSerializer, RegisterSerializer, EditAccessLayerSerializer
from users.models import Profile, Group


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
            request.user.group.members.add(user)
            request.user.group.save()
            user.save()

            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=501)
    else:
        return Response(status=401)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_info(request):
    date = datetime.date.today()
    user = request.user
    try:
        if user.group_member.group and type(user.group_member.group.tariff_exp) == NoneType:
            return Response({
                'error': 'tariff expired or don\'t have any tariff'
            })
        if user.group_member.group.tariff_exp <= date:
            user.group_member.group.tariff_level = 0
            user.group_member.group.tariff_exp = None
            user.group_member.group.volume = 0
            user.group_member.group.save()
            user.group_member.save()
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
    except TypeError:
        return Response({
                'error': 'tariff expired or don\'t have any tariff'
            })
    except django.contrib.auth.models.User.group.RelatedObjectDoesNotExist:
        group = user.group_member.first()
        if group.tariff_exp <= date:
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
                'group_id': group.id,
            }
            return Response(response)
        pass


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_group_members(request):
    group = request.user.group_member.first()
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
        user = User.objects.filter(username=username).first()
        try:
            user.delete()
        except AttributeError as e:
            return Response(data={"error": "Not Found",
                                  'details': str(e),
                                  'snippet': f'Maybe DB don\'t have user with username "{username}"'},
                            status=404)
        return Response(data=user.id, status=201)
    else:
        return Response(status=401)
