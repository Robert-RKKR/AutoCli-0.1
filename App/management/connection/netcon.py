# Python Import:
import time

# Netmiko Import:
from netmiko import ConnectHandler
from netmiko.ssh_exception import  AuthenticationException
from netmiko.ssh_exception import NetMikoTimeoutException
from paramiko.ssh_exception import SSHException

# Application Import:
from logger.logger import Logger
from management.models import Device


class NetCon:

    # Logger class initiation:
    logger = Logger('NetCon')

    def __init__(self, device: Device) -> None:
        """
            The NetCon class uses netmiko library, to establish a SSH connection with networks devices.

                Class attributes:
                -----------------
                device: Device object
                    Description
                
                Methods:
                --------
                send_command: (command)
                    Description
                config_commands: (response)
                    Description
        """
        # Device declaration:
        self.device = device

        # Connection status:
        self.status = None

        # Execution timer:
        self.execution_time = None

        # Check if device is Device object:
        if isinstance(device, Device):
            # Change device type name to netmiko name:
            if self.device.device_type == 0:
                self.device_type = 'autodetect'
            elif self.device.device_type == 1:
                self.device_type = 'cisco_ios'
            elif self.device.device_type == 2:
                self.device_type = 'cisco_xr'
            elif self.device.device_type == 3:
                self.device_type = 'cisco_xe'
            elif self.device.device_type == 4:
                self.device_type = 'cisco_nxos'
        else:
            self.status = False # Change connection status to False.
            raise ConnectionError

        # Try connect to device:
        try:
            # Log start of SSH connection:
            NetCon.logger.debug('SSH connection has been started.', self)
            self.connection = ConnectHandler(**{
                'device_type': self.device_type,
                'host': self.device.hostname,
                'username': self.device.credential.username,
                'password': self.device.credential.password,
                'port': self.device.ssh_port,
                'secret': self.device.credential.password,
            })
            NetCon.logger.info('SSH connection has been established.', self)
            self.status = True # Change connection status to True:

        # Handel exceptions:
        except AuthenticationException as error:
            NetCon.logger.error(error, self)
            self.status = False # Change connection status to False.
        except NetMikoTimeoutException as error:
            NetCon.logger.error(error, self)
            self.status = False # Change connection status to False.
        except SSHException as error:
            NetCon.logger.error(error, self)
            self.status = False # Change connection status to False.

    def __del__(self):
        """ End of SSH connection """
        NetCon.logger.info('SSH session ended.', self)

    def __repr__(self) -> str:
        """ Connection class representation is IP address and port number of Https server. """
        return self.device.hostname

    def send_command(self, command) -> str:
        """ 
            Takes list of strings or string (Networks commands), and send to network device using SSH protocol.
            Usable only with enable levels commends.
        """

        # Check connection status:
        if self.status is False:
            NetCon.logger.error('No connection available.', self)
            return None

        else:
            # Start clock count:
            start_time = time.perf_counter()

            # Collect data from device:
            return_data = None

            # Try to sent command into network device:
            try:
                # Collect data from device:
                NetCon.logger.debug('The sending of a new CLI command has been started.', self, {'command': command})
                if isinstance(command, list):
                    for one_command in command:
                        return_data = self.connection.send_command(one_command)
                else:
                    return_data = self.connection.send_command(command)
                NetCon.logger.debug('The CLI command has been sent.', self)
            except UnboundLocalError as error:
                NetCon.logger.error(error, self)
                return error

            # Finish clock count & method execution time:
            finish_time = time.perf_counter()
            self.execution_time = round(finish_time - start_time, 5)
            
            # Return data:
            return return_data

    def config_commands(self, command) -> str:
        """ 
            Takes list of strings or string (Networks commands), and send to network device using SSH protocol.
            Usable only with configuration terminal levels commends.
        """

        # Check connection status:
        if self.status is False:
            NetCon.logger.error('No connection available.', self)
            return None

        else:
            # Start clock count:
            start_time = time.perf_counter()

            # Collect data from device:
            return_data = None

            # Try to sent command into network device:
            try:
                NetCon.logger.debug('The sending of a new CLI command has started.', self, {'command': command})
                return_data = self.connection.send_config_set(command)
                NetCon.logger.debug('The CLI command has been sent.', self)
            except UnboundLocalError as error:
                NetCon.logger.error(error, self)
                return error
            except:
                NetCon.logger.error('CLI command error.', self)

            # Finish clock count & method execution time:
            finish_time = time.perf_counter()
            self.execution_time = round(finish_time - start_time, 5)

            # Return data:
            return return_data