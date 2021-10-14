# Rest Django Import:
from rest_framework import serializers

# Application Import:
from management.models import (
    Device,
)

class DeviceGetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Device
        fields = [
            'id', 'status', 'created', 'updated',
            'name', 'hostname', 'device_type', 'ico', 'ssh_port', 'https_port', 'description',
            'credential', 'secret', 'token', 'certificate',
            'ssh_status', 'https_status', 'ping_status',
            
        ]


class DevicePostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Device
        fields = [
            'name', 'status', 'hostname', 'device_type',
            'credential', 'ico', 'ssh_port',
            'https_port', 'certificate', 'description',
        ]