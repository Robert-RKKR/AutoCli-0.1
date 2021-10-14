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
    output = restcon.get('restconf')

    if restcon.status is True:
        device.https_status = True
        device.ssh_status = True
        device.ping_status = True
        device.save()
    else:
        device.https_status = False
        device.ssh_status = False
        device.ping_status = False
        device.save()

    self.update_state(state='Ending')

    return output

@shared_task
def test_update_all():
    devices = Device.objects.all()

    for device in devices:
        task_simple.delay(device.id)


@shared_task(bind=True, track_started=True)
def update_all(self):

    devices = Device.objects.all()

    self.update_state(state='Starting')

    for device in devices:
        restcon = RestCon(device)
        output = restcon.get('restconf')

        if restcon.status is True:
            device.https_status = True
            device.ssh_status = True
            device.ping_status = True
            device.save()
        else:
            device.https_status = False
            device.ssh_status = False
            device.ping_status = False
            device.save()



    self.update_state(state='Ending')


    """devices = Device.objects.all()

    self.update_state(state='Starting')

    for device in devices:
        task_simple.delay(device.id)

    self.update_state(state='Ending')"""


class ConnectionManager:

    def __init__(self, device_list: list) -> None:
        self.device_list = device_list