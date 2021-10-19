from django.urls import path
from . import views

urlpatterns = [
    # Device API:
    path('device/all', views.DeviceAllAPI.as_view(), name='device_all'),
    path('device/<int:id>', views.DeviceOneAPI.as_view(), name='device_one'),
    path('device/add', views.DeviceAddAPI.as_view(), name='device_add'),

    # Logger API:
    path('loggerdata/last', views.LoggerDataLastAPI.as_view(), name='loggerdata_last'),
    path('loggerdata/search/<str:key>=<str:value>', views.LoggerDataSearchAPI.as_view(), name='loggerdata_search'),
]