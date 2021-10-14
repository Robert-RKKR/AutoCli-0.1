from django.urls import path
from . import views

urlpatterns = [
    path('device/all', views.DeviceAllAPI.as_view(), name='device_all'),
    path('device/<int:id>', views.DeviceOneAPI.as_view(), name='device_one'),
    path('device/add', views.DeviceAddAPI.as_view(), name='device_add'),
]