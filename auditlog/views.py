from datetime import datetime
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from auditlog.models import AuditLogModel
from rest_framework.response import Response

from auditlog.serializers import ActionFileSerializer

# Create your views here.

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def action(request):
    serialized = ActionFileSerializer(data=request.data)
    if serialized.is_valid():
        action = AuditLogModel(
            file_name=serialized.data.get('filename'),
            action=serialized.data.get('action'),
            user=request.user.username,
            group=request.user.group,
            datestamp=serialized.data.get('datestamp'),
            comment = serialized.data.get('comment') if serialized.data.get('comment') else None
        )
        action.save()
        response = {
            'file_name': action.file_name,
            'action': action.action,
            'user': action.user,
            'group': action.group,
            'datestamp': action.datestamp,
            'comment': action.comment,
        }
    return Response(response)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_history(request):
    #timedelta = None
    #if request.GET.get('timedelta'):
    #    timedelta = request.GET.get('timedelta')
    group = request.user.group
    result = AuditLogModel.objects.filter(group=group)
    #if timedelta: result.filter()
    print(result)
    return Response(result)

    

