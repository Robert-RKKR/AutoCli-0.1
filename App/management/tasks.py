# Python Import:
import os

# Application Import:
from .connection.netcon import NetCon
from .connection.restcon import RestCon
from .models import Device, DeviceData

# Celery Import:
from celery import shared_task


# Task device related:
@shared_task(bind=True, track_started=True)
def single_device_check(self, device_id: int) -> bool:
    """
        Check if device is available by using HTTPS request at the beginning,
        and an SSH connection if the HTTPS request fails.
    """
    # Single device check status:
    status = None

    # Check if device_id variable is intiger:
    if isinstance(device_id, int):
        
        # Find Device object by ID:
        device = Device.objects.get(id=device_id)
            
        # Connect to device using HTTPS request:
        https_connection = RestCon(device)
        https_output = https_connection.get('restconf')

        # Check HTTPS request output and change device status:
        if https_connection.status is True:
            device.https_status = True
            device.ssh_status = True
            device.save()
        else:
            device.https_status = False
            device.ssh_status = False
            device.save()

        # Connect to device using SSH connection:
        ssh_connection = None

    else: # If device variable is not a intiger, raise type error:
        raise TypeError('device variable can only be a intiger.')

    # Return single device check status:
    return status


#@shared_task(bind=True, track_started=True)
def single_device_collect(device_id: int) -> bool:
    """
        Collect data from device.
    """
    # Active devices check status:
    status = None

    # Check if device_id variable is intiger:
    if isinstance(device_id, int):

        # Find Device object by ID:
        device = Device.objects.get(id=device_id)

        # Connect to device using HTTPS:
        https_connection = RestCon(device)
        native_output = https_connection.get('restconf/data/Cisco-IOS-XE-native:native')

        # Save collected data:
        native = native_output.get('Cisco-IOS-XE-native:native', None)
        if native is None:
            native = {}

        device_data = {
            # Corelation witch device model:
            'device': device,

            # Basic device information:
            'hostname': native.get('hostname', None),
            'system_version': native.get('version', None),
        }

        """domain_name = native.get('', None)
            default_gateway = native.get('', None)
            name_server_list = native.get('', None)
            ntp_server_list = native.get('', None)
            os_boot_files_list = native.get('', None)
            ios_users_list = native.get('', None)

            # SNMP protocol information:
            snmp_server_community_list = native.get('', None)
            snmp_server_group_list = native.get('', None)
            snmp_server_user_list = native.get('', None)

            # STP protocol information:
            spanning_tree_mode = native.get('', None)"""

        device_data_model = DeviceData.objects.create(**device_data)


    else: # If device variable is not a intiger, raise type error:
        raise TypeError('device variable can only be a intiger.')


@shared_task(bind=True, track_started=True)
def active_devices_check(self) -> bool:
    """
        Check all active devices if the are available by using HTTPS request at the beginning,
        and an SSH connection if the HTTPS request fails.
    """
    # Active devices check status:
    status = None
        
    # Collect all active devices:
    devices = Device.objects.filter(status=True)

    # Iterate thru all active devices:
    for device in devices:
            
        # Check device status:
        single_device_check.delay(device.id)

    # Return active devices check status:
    return status


class ConnectionManager:

    def __init__(self, device_list: list) -> None:
        self.device_list = device_list