# Application Import:
from posixpath import split
from .netcon import NetCon
from .restcon import RestCon
from ..models import Device, DeviceData

class ConnectionManager:

    def __init__(self, device: Device) -> Device:
        self.device = device

        # Main data dictionary:
        self.device_data = {}

    def collect_data(self):
        """
            Description.
        """
        if self.device.https_status is True:
            # Connect to device using HTTPS:
            https_connection = RestCon(self.device)
            https_connection.get('restconf')
            if https_connection.json_status is True:
                self.__cisco_ios_xe(https_connection)
            else:
                self.__cisco_nx_os(https_connection)
        elif self.device.ssh_status is True:
            self.__cisco_ssh()


    def __cisco_ssh(self):
        print('---> SSH CONNECTION')
        

    def __cisco_ios_xe(self, https_connection):
        """
            Description.
        """
        # Collect all data from device:
        self.device_data['Cisco-IOS-XE-native'] = https_connection.get(
            'restconf/data/Cisco-IOS-XE-native:native')
        self.device_data['Cisco-IOS-XE-platform-software-oper'] = https_connection.get(
            'restconf/data/Cisco-IOS-XE-platform-software-oper:cisco-platform-software')

        """self.device_data['Cisco-IOS-XE-device-hardware-oper'] = https_connection.get(
            'restconf/data/Cisco-IOS-XE-device-hardware-oper:device-hardware-data')
        self.device_data['Cisco-IOS-XE-install-oper'] = https_connection.get(
            'restconf/data/Cisco-IOS-XE-install-oper:install-oper-data')
        self.device_data['Cisco-IOS-XE-memory-oper'] = https_connection.get(
            'restconf/data/Cisco-IOS-XE-memory-oper:memory-statistics')"""
  
        update_data = {
            # Corelation witch device model:
            'device': self.device,
            # Cisco-IOS-XE-native:
            'hostname': self.__collect(
                'Cisco-IOS-XE-native/Cisco-IOS-XE-native:native/hostname'),
            'system_version': self.__collect(
                'Cisco-IOS-XE-native/Cisco-IOS-XE-native:native/version'),
            'domain_name': self.__collect(
                'Cisco-IOS-XE-native/Cisco-IOS-XE-native:native/ip/domain/name'),
            'default_gateway': self.__collect(
                'Cisco-IOS-XE-native/Cisco-IOS-XE-native:native/ip/default-gateway'),
            'name_server_list': self.__collect(
                'Cisco-IOS-XE-native/Cisco-IOS-XE-native:native/ip/name-server/no-vrf'),
            'ntp_server_list': self.__collect(
                'Cisco-IOS-XE-native/Cisco-IOS-XE-native:native/ntp/Cisco-IOS-XE-ntp:server/server-list'),
            'os_boot_files_list': self.__collect(
                'Cisco-IOS-XE-native/Cisco-IOS-XE-native:native/boot/system/bootfile/filename-list'),
            'ios_users_list': self.__collect(
                'Cisco-IOS-XE-native/Cisco-IOS-XE-native:native/username'),
            'snmp_server_community_list': self.__collect(
                'Cisco-IOS-XE-native/Cisco-IOS-XE-native:native/snmp-server/Cisco-IOS-XE-snmp:community-config'),
            'snmp_server_group_list': self.__collect(
                'Cisco-IOS-XE-native/Cisco-IOS-XE-native:native/snmp-server/Cisco-IOS-XE-snmp:group'),
            'snmp_server_user_list': self.__collect(
                'Cisco-IOS-XE-native/Cisco-IOS-XE-native:native/snmp-server/Cisco-IOS-XE-snmp:user/names'),
            'spanning_tree_mode': self.__collect(
                'Cisco-IOS-XE-native/Cisco-IOS-XE-native:native/spanning-tree/Cisco-IOS-XE-spanning-tree:mode'),
            # Cisco-IOS-XE-platform-software-oper:
            'memory_stats': self.__collect(
                'Cisco-IOS-XE-platform-software-oper/Cisco-IOS-XE-platform-software-oper:cisco-platform-software/control-processes/control-process/LIST/memory-stats'),
            'cpu_stats': self.__collect(
                'Cisco-IOS-XE-platform-software-oper/Cisco-IOS-XE-platform-software-oper:cisco-platform-software/control-processes/control-process/LIST/per-core-stats/per-core-stat'),
        }

        return DeviceData.objects.create(**update_data)


    def __cisco_nx_os(self, https_connection):
        """
            Description.
        """
        print('--->', https_connection)


    def __collect(self, path: str):
        """
            Collect data from dictionary, based on string keys separated by '/'.
        """
        # Convert string path to list of dictionary keys:
        path_list = path.split('/')
        current_dict = self.device_data

        iterate = 0

        # Iterate thru all keys taken from path list:
        for row in path_list:
            
            # Check if key is have a special meaning:
            if row == 'LIST':
                # Not used key:
                rest_of_keys = path_list[iterate+1:]
                # Output list:
                output = []
                # Iterate thru all elements of LIST:
                for element in current_dict:
                    # Iterate thru all rest of keys:
                    for under_row in rest_of_keys:
                        # Try to collect data using key from path list:
                        try:
                            data = element[under_row]
                            element = data
                        except KeyError:
                            return None     
                    output.append(element)
                return output
            else:
                # Try to collect data using key from path list:
                try:
                    data = current_dict[row]
                    current_dict = data
                except KeyError:
                    return None

            iterate += 1

        return current_dict