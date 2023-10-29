from rest_framework import serializers

from api.models import Storage


class StorageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Storage
        fields = '__all__'


class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()
    access_layer = serializers.IntegerField()


class EditAccessLayerSerializer(serializers.Serializer):
    username = serializers.CharField()
    access_layer = serializers.IntegerField()




