# Django Import:
from django.contrib import admin

# Applications Import:
from .models import (
    Template,
    AutomationPolicy,
    TaskManager,
    Scheduler,
    TemplateAutomationPolicyRelation,
    DeviceAutomationPolicyRelation,
)

# Admin classes:
@admin.register(Template)
class TemplateAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'created', 'updated',
    )
    search_fields = (
        'name', 'created', 'updated',
    )


@admin.register(AutomationPolicy)
class AutomationPolicyAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'created', 'updated', 'scheduler',
    )
    search_fields = (
        'name', 'created', 'updated',
    )


@admin.register(TaskManager)
class TaskManagerAdmin(admin.ModelAdmin):
    list_display = (
        'pk', 'automation_policy', 'created', 'updated',
    )
    search_fields = (
        'pk',
    )


@admin.register(Scheduler)
class SchedulerAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'execute_time', 'execute_date', 'created', 'updated',
    )
    search_fields = (
        'name', 'created', 'updated',
    )


@admin.register(TemplateAutomationPolicyRelation)
class TemplateAutomationPolicyRelationAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'template', 'automation_policy', 'sequence',
    )
    search_fields = (
        'template', 'automation_policy',
    )


@admin.register(DeviceAutomationPolicyRelation)
class GDeviceAutomationPolicyRelationAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'device', 'automation_policy', 'sequence',
    )
    search_fields = (
        'device', 'automation_policy',
    )