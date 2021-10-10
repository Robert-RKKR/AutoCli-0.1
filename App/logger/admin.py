from django.contrib import admin
from .models import LoggerData, AdditionalData


# Admins views:
@admin.register(LoggerData)
class LoggerDataAdmin(admin.ModelAdmin):
    list_display = (
        'timestamp', 'message',
    )
    search_fields = (
        'timestamp', 'process', 'application', 'module', 'severity', 'message',
    )
    list_filter = (
        'severity',
    )

@admin.register(AdditionalData)
class AdditionalDataAdmin(admin.ModelAdmin):
    list_display = (
        'logger', 'name', 'value',
    )
    search_fields = (
        'logger', 'name', 'value',
    )