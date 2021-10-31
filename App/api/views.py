# Django Import:
from django.shortcuts import get_object_or_404

# Rest Django Import:
from rest_framework import generics

# Serializers Import:
from .serializers import (
    DeviceGetSerializer,
    DeviceSimplePostSerializer,
    DeviceComplexPostSerializer,
    CredentialDataGetSerializer,
    LoggerDataGetSerializer,
)


from .pagination import (
    SmallResultsSetPagination,
    MediumResultsSetPagination,
    BigResultsSetPagination
)

# Models Import:
from logger.models import LoggerData
from management.models import (
    Device, Credential,
)

# ALL Device Views:
class DeviceAllAPI(generics.ListAPIView):
    queryset = Device.active.all().order_by('id')
    serializer_class = DeviceGetSerializer
    pagination_class = SmallResultsSetPagination


class DeviceOneAPI(generics.RetrieveAPIView):
    lookup_field = 'id'
    queryset = Device.objects.all()
    serializer_class = DeviceGetSerializer


class DeviceSimpleAddAPI(generics.CreateAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSimplePostSerializer


class DeviceComplexAddAPI(generics.CreateAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceComplexPostSerializer


# ALL Credentials Views:
class CredentialAllAPI(generics.ListAPIView):
    queryset = Credential.objects.all().order_by('id')
    serializer_class = CredentialDataGetSerializer
    pagination_class = SmallResultsSetPagination


# ALL Logger Views:
class LoggerDataLastAPI(generics.ListAPIView):
    queryset = LoggerData.objects.all().order_by('-id')
    serializer_class = LoggerDataGetSerializer
    pagination_class = MediumResultsSetPagination


class LoggerDataSearchAPI(generics.ListAPIView):
    serializer_class = LoggerDataGetSerializer
    pagination_class = SmallResultsSetPagination

    def get_queryset(self):
        key = self.kwargs['key']
        value = self.kwargs['value']
        output = LoggerData.objects.filter(**{key: value}).order_by('-id')
        return output




"""
    class LoggerTest(generics.ListAPIView):
    queryset = LoggerData.objects.all()
    serializer_class = LoggerDataGetSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['application', 'module', 'severity']
    ordering = ['-timestamp']
    
    
    class LoggerDataLastHundredModuleSpecificAPI(generics.ListAPIView):
    serializer_class = LoggerDataGetSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['module', 'severity']
    ordering = ['-id']
    paginate_by = 30

    def get_queryset(self):
        module = self.kwargs['module']
        return LoggerData.objects.filter(module=module)
    
    """