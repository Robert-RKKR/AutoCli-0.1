from django.urls import path
from . import views
from .views import (
    login_page,
)

urlpatterns = [
    path('login_page', login_page),
]