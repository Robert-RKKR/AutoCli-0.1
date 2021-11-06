# Application Import:
from .connection.netcon import NetCon
from .connection.restcon import RestCon
from .connection.connection_manager import ConnectionManager
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
        https_connection.get('restconf')

        # Check HTTPS request output and change device status:
        if https_connection.status is True:
            device.https_status = True
            device.ssh_status = True
            device.save()
        else:
            # Connect to device using SSH connection:
            ssh_connection = NetCon(device)
        
            # Check SSH request output and change device status:
            if ssh_connection.status is True:
                device.https_status = False
                device.ssh_status = True
                device.save()
            else:
                device.https_status = False
                device.ssh_status = False
                device.save()

    else: # If device variable is not a intiger, raise type error:
        raise TypeError('Device variable can only be a intiger.')

    # Return single device check status:
    return status
    

@shared_task(bind=True, track_started=True)
def single_device_collect(self, device_id: int) -> bool:
    """
        Collect data from device.
    """
    # Active devices check status:
    status = None

    # Check if device_id variable is intiger:
    if isinstance(device_id, int):

        # Find Device object by ID:
        device = Device.objects.get(id=device_id)

        # Run connection manager to collect all data:
        collector = ConnectionManager(device)
        collector.collect_data()

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


@shared_task(bind=True, track_started=True)
def send_commands(self, device_id: int, commands: list) -> bool:

    # Single device check status:
    status = None

    # Check if device_id variable is intiger:
    if isinstance(device_id, int) and isinstance(commands, list):
        
        # Find Device object by ID:
        device = Device.objects.get(id=device_id)

        # Connect to device using SSH connection:
        ssh_connection = NetCon(device)

        # Sends commands:
        output = ssh_connection.config_commands(commands)

    else: # If device variable is not a intiger, raise type error:
        raise TypeError('Device variable can only be a intiger or commands variable can only be a list.')

    # Return single device check status:
    return output