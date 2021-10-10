from django.urls import path
from . import views

urlpatterns = [
    path('device/all', views.DeviceAllAPI.as_view(), name='device_all'),
    path('device/add', views.DeviceAddAPI.as_view(), name='device_add'),
]