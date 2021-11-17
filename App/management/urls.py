from django.urls import path
from . import views
from .views import (
    Test, Testing,
    devices_search,
    device, device_add,
    logger_search,
)

urlpatterns = [
    path('devices_search', devices_search),
    path('logger_search', logger_search),
    path('device/<int:pk>', device),
    path('device_add', device_add),
    path('test', Test.as_view()),
    path('testing', Testing.as_view()),
]