# Django Import:
from os import name
from django.contrib import admin, messages
from django.utils.translation import ngettext

# Applications Import:
from .models import (
    TagDeviceRelation, Credential,
    Tag, Device, DeviceData, SshDeviceData,
    TestDevice, TestSshDevice, TestHttpsDevice,
)

admin.site.register(TestDevice)
admin.site.register(TestSshDevice)
admin.site.register(TestHttpsDevice)

# Admin classes:
@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    empty_value_display = '-None-'
    actions = (
        'make_nonactive', 'make_active', 
    )
    list_display = (
        'name', 'hostname', 'ssh_status',
        'https_status',
    )
    list_filter = (
        'status', 'device_type', 'credential',
    )
    search_fields = (
        'name', 'hostname',
    )
    ordering = (
        'name', 'hostname',
    )
    fields = (
        'status',
        ('name', 'hostname'),
        ('device_type', 'ico'),
        ('ssh_port', 'https_port'),
        ('credential', 'secret', 'token'),
        'certificate',
        'description',
    )

    @admin.action(description='Make device nonactive')
    def make_nonactive(self, request, queryset):
        change = queryset.update(status=0)

        self.message_user(request, ngettext(
            '%d device was successfully marked as nonactive.',
            '%d devices were successfully marked as nonactive.',
            change,
        ) % change, messages.SUCCESS)

    @admin.action(description='Make device active')
    def make_active(self, request, queryset):
        change = queryset.update(status=1)

        self.message_user(request, ngettext(
            '%d device was successfully marked as active.',
            '%d devices were successfully marked as active.',
            change,
        ) % change, messages.SUCCESS)


@admin.register(DeviceData)
class CredentialAdmin(admin.ModelAdmin):
    list_display = (
        'device', 'created', 'hostname', 'system_version',
    )
    search_fields = (
        'device', 'created',
    )


@admin.register(SshDeviceData)
class CredentialAdmin(admin.ModelAdmin):
    list_display = (
        'device', 'created', 'hostname', 'version',
    )
    search_fields = (
        'device', 'created', 'version',
    )


@admin.register(Credential)
class CredentialAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'username', 'password', 'description',
    )
    search_fields = (
        'name', 'username',
    )


@admin.register(Tag)
class ColorAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'color', 'description',
    )
    search_fields = (
        'name', 'color',
    )


@admin.register(TagDeviceRelation)
class GroupDeviceRelationAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'device', 'tag', 'created',
    )
    search_fields = (
        'device', 'tag',
    )