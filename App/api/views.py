# Django Import:
from django.shortcuts import render

# Rest Django Import:
from rest_framework import generics

# Application Import:
from .serializers import (
    DeviceGetSerializer,
    DevicePostSerializer,
)
from management.models import (
    Device,
)

# ALL Device Views:
class DeviceAllAPI(generics.ListAPIView):
    queryset = Device.active.all().order_by('id')
    serializer_class = DeviceGetSerializer

class DeviceOneAPI(generics.RetrieveAPIView):
    lookup_field = 'id'
    queryset = Device.objects.all()
    serializer_class = DeviceGetSerializer

class DeviceAddAPI(generics.CreateAPIView):
    queryset = Device.objects.all()
    serializer_class = DevicePostSerializer