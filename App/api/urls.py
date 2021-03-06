from django.urls import path
from . import views

urlpatterns = [
    # Device API:
    path('device/all', views.DeviceAllAPI.as_view(), name='device_all'),
    path('device/<int:id>', views.DeviceOneAPI.as_view(), name='device_one'),
    path('device/add', views.DeviceSimpleAddAPI.as_view(), name='device_add_simple'),
    path('device/complex_add', views.DeviceComplexAddAPI.as_view(), name='device_add_complex'),

    # Device SSH Data API:
    path('device/ssh', views.SshDeviceDataAllAPI.as_view(), name='device_ssh'),
    path('device/ssh/<int:device_id>', views.SshDeviceDataOneAPI.as_view(), name='device_ssh_one'),

    # Tag API:
    path('tag-device/all', views.TagDeviceAllAPI.as_view(), name='tag_device_all'),

    # Credential API:
    path('credential/all', views.CredentialAllAPI.as_view(), name='credential_all'),

    # Logger API:
    path('loggerdata/last', views.LoggerDataLastAPI.as_view(), name='loggerdata_last'),
    path('loggerdata/search/<str:key>=<str:value>', views.LoggerDataSearchAPI.as_view(), name='loggerdata_search'),
]