# Django Import:
from django.db import models

# Celery Import:
from django_celery_beat.models import PeriodicTask, PeriodicTasks

# Applications Import:
from management.models import Device

# Automations models.
class Template(models.Model):
    # Creation data:
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # Basic data:
    name = models.CharField(max_length=32, blank=False, unique=True)
    description = models.CharField(max_length=512, default="Template description")

    # Template body:
    value = models.TextField(blank=False)
    variables = models.JSONField(null=True)

    def __str__(self) -> str:
        return self.name


class AutomationPolicy(models.Model):
    # Creation data:
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # Basic data:
    name = models.CharField(max_length=32, blank=False, unique=True)
    description = models.CharField(max_length=512, default="Automation policy description")

    # Scheduler data:
    scheduler = models.ForeignKey('Scheduler', on_delete=models.PROTECT)

    def __str__(self) -> str:
        return self.name


class TaskManager(models.Model):
    # Creation data:
    status = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # Automation policy data:
    automation_policy = models.ForeignKey(AutomationPolicy, on_delete=models.PROTECT)

    # Task data:
    input_data = models.TextField(null=True)
    output_data = models.TextField(null=True)

    def __str__(self) -> str:
        return self.pk


class Scheduler(models.Model):
    # Creation data:
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # Basic data:
    name = models.CharField(max_length=32, blank=False, unique=True)
    description = models.CharField(max_length=512, default="Scheduler description")

    # Execute data:
    execute_time = models.TimeField(null=True, blank=True)
    execute_date = models.DateTimeField(null=True, blank=True)
    seconds = models.IntegerField(null=True, blank=True)

    def __str__(self) -> str:
        return self.name

    """class Meta:
        
        constraints = [
            models.CheckConstraint(
                name = '%(app_label)s_%(class)s_value_matches_type',
                check = (
                    models.Q(
                        seconds__isnull = False,
                        execute_time__isnull = False,
                        execute_date__isnull = True,
                    )
                    | models.Q(
                        seconds__isnull = False,
                        execute_time__isnull = True,
                        execute_date__isnull = False,
                    )
                    | models.Q(
                        seconds__isnull = True,
                        execute_time__isnull = False,
                        execute_date__isnull = False,
                    )
                ),
            )
        ]"""


# Relations models:
class TemplateAutomationPolicyRelation(models.Model):
    template = models.ForeignKey(Template, on_delete=models.PROTECT)
    automation_policy = models.ForeignKey(AutomationPolicy, on_delete=models.PROTECT)
    sequence = models.IntegerField(unique=True, blank=False)

    class Meta:
        unique_together = [['template', 'automation_policy']]


class DeviceAutomationPolicyRelation(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    automation_policy = models.ForeignKey(AutomationPolicy, on_delete=models.PROTECT)
    sequence = models.IntegerField(unique=True, blank=False)

    class Meta:
        unique_together = [['device', 'automation_policy']]
