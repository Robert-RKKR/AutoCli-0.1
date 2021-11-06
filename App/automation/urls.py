from django.urls import path
from . import views
from .views import (
    template, template_search,
)

urlpatterns = [
    path('template/<int:id>', template),
    path('template_search', template_search),
]