# Python Import:
import os

# Application Import:
from connection.netcon import NetCon
from connection.restcon import RestCon
from .models import Device

# Celery Import:
from celery import shared_task


@shared_task(bind=True, track_started=True)
def task_simple(self, id):

    device = Device.objects.get(id=id)

    self.update_state(state='Starting')

    restcon = RestCon(device)
    output = restcon.get('restconf/data/Cisco-IOS-XE-native:native/hostname')

    if isinstance(output, dict):
        for row in output:
            device.secret = str(output[row])
            device.save()

    if restcon.status is True:
        device.https_status = True
        device.save()

    self.update_state(state='Ending')

    return output


class ConnectionManager:

    def __init__(self, device_list: list) -> None:
        self.device_list = device_list