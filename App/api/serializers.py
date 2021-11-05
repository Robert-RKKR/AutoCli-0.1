# Rest Django Import:
from rest_framework import serializers

# Application Import:
from logger.models import LoggerData
from management.models import (
    Device, Credential, Tag,
)


# Tag serializers:
class TagGetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        ordering = ['name']
        fields = [
            'name', 'color', 'description', 'devices',
        ]
        extra_kwargs = {'devices': {'required': False}}


# Device serializers:
class DeviceGetSerializer(serializers.ModelSerializer):
    tags = TagGetSerializer(many=True, read_only=True)

    class Meta:
        model = Device
        fields = [
            'id', 'status', 'created', 'updated',
            'name', 'hostname', 'device_type', 'ico', 'ssh_port', 'https_port', 'description',
            'credential', 'secret', 'token', 'certificate',
            'ssh_status', 'https_status', 'tags',   
        ]
        extra_kwargs = {'tags': {'required': False}}


class DeviceSimplePostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Device
        fields = [
            'name', 'hostname',
        ]


class DeviceComplexPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Device
        fields = [
            'name', 'status', 'hostname', 'device_type',
            'credential', 'ico', 'ssh_port',
            'https_port', 'certificate', 'description',
        ]


# Credentials serializers:
class CredentialDataGetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Credential
        fields = [
            'name', 'username', 'password', 'secret',
            'token', 'description', 'created', 'updated',
        ]


# Logerg serializers:
class LoggerDataGetSerializer(serializers.ModelSerializer):

    class Meta:
        model = LoggerData
        fields = [
            'id', 'timestamp', 'process', 'application',
            'module', 'severity', 'message',
        ]