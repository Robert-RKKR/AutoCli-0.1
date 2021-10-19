""" Python Import:
import os

# Application Import:
from .netcon import NetCon
from .restcon import RestCon

# Celery Import:
from celery import shared_task

def check_ping(ip_address):
    ping_result = os.system(f"ping -c 5 {ip_address}")
    print(ping_result)

@shared_task(bind=True, track_started=True)
def check_ssh(self, id):
    

    device = Device.objects.get(id=id)

    self.update_state(state='Starting')

    restcon = RestCon(device)
    output = restcon.get('restconf/data/Cisco-IOS-XE-platform-software-oper:cisco-platform-software')

    if restcon.status is True:
        device.https_status = True
        device.save()

    self.update_state(state='Ending')

    return output


class ConnectionManager:

    def __init__(self, device_list: list) -> None:
        self.device_list = device_list"""