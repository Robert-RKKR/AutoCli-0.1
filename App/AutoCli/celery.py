from celery import Celery
import os

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'AutoCli.settings')

app = Celery('AutoCli')

# Celery settings are in settings.py using a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

"""app.conf.beat_schedule = {
    'update_all_device_every_300s': {
        'task': 'management.tasks.active_devices_check',
        'schedule': 300.0,
    }
}"""
#from automation.automation.scheduler import scheduler_creator
#app.conf.beat_schedule = scheduler_creator()

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')