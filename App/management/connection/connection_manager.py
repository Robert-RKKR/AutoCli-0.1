# Python Import:
import os

# Application Import:
from .netcon import NetCon

def check_ping(ip_address):
    ping_result = os.system(f"ping -c 5 {ip_address}")
    print(ping_result)


def check_ssh(device):
    connection = NetCon(device)
    output = connection.send_command('show version')
    print(output)

    if connection.status is True:
        device.ssh_status = True
        device.save()
    return connection


class ConnectionManager:

    def __init__(self, device_list: list) -> None:
        self.device_list = device_list