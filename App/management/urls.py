from django.urls import path
from . import views
from .views import (
    Test,
    Testing,
    devices_search,
    device,
)

urlpatterns = [
    path('devices_search', devices_search),
    path('device/<str:id>', device),
    path('test', Test.as_view()),
    path('testing', Testing.as_view()),
]