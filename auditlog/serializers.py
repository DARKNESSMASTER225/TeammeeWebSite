from rest_framework import serializers

from auditlog.models import AuditLogModel

class ActionFileSerializer(serializers.ModelSerializer):
    comment = serializers.CharField(max_length=150, required=False)
    class Meta:
        model = AuditLogModel
        fields = ['file_name', 'action', 'datestamp', 'comment']


class ActionFileModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuditLogModel
        fields = '__all__'