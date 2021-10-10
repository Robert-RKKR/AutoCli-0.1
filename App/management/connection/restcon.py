# Python Import:
import requests
import json

# Application Import:
from logger.logger import Logger
from ..models import Device


class RestCon:
    
    # Logger class initiation:
    logger = Logger('NetCon')

    def __init__(self, device: Device) -> None:
        """
            The RestCon class uses requests library, to connect with Https server for API connections.

            Class attributes:
                -----------------
                device: Device object
                    Description

            Methods:
            --------
            connect: (url, connectionType="GET", payload=None)
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
            pass
        else:
            self.status = False # Change connection status to False.
            raise ConnectionError

    def __repr__(self):
        """ Connection class representation is IP address and port number of Https server. """
        
        # Check connection status:
        if self.status is False:
            return None
        else:
            return f"{self.device.hostname}:{self.device.ssh_port}"

    def get(self, url, headers: str = None, payload: str = None):
        """
            Send HTTPS GET request.

            Parameters:
            -----------
            url: string
                URL string used to construct HTTPS request.
            payload: string
                Additional data used to construct HTTPS request.

            return:
            -------
            jsonResponse: dict
                Return date collected from HTTPS server.
        """

        # Create URL Address frome tamplate:
        request_url = f"""https://{self.device.hostname}:{self.device.https_port}/{url}"""

        # Try to connect with device:
        try:
            # Log starting of a new connection to https server:
            RestCon.logger.info("Starting a new Https connection.", self)

            # Connect to https server with password and username or by token:
            if self.device.token:
                response = requests.get(
                    request_url,
                    headers=headers,
                    data=payload,
                    verify=self.device.certificate,
                )
            else: # Token inside header:
                response = requests.get(
                    request_url,
                    headers=headers,
                    auth=(self.device.credential.username, self.device.credential.password),
                    data=payload,
                    verify=self.device.certificate,
                )
                
            # Convert HTTPS response:
            self.__connect(response)

        except requests.exceptions.SSLError as error:
            RestCon.logger.error(error, self)
            # Change connection status to False:
            self.status = False
            return self.status

        except requests.exceptions.Timeout as error:
            RestCon.logger.error(error, self) 
            # Change connection status to False:
            self.status = False
            return self.status

        except requests.exceptions.InvalidURL as error:
            RestCon.logger.error(error, self)        
            # Change connection status to False:
            self.status = False
            return self.status

    def __connect(self, response):
        """
            Convert HTTPS response to ridable data.

            Parameters:
            -----------
            response: 
                Description
        """
            
        # Log when https connection was established:
        RestCon.logger.debug("Https connection was established.", self)
            
        # Try to convert response to python dictionary:
        try:
            jsonResponse = json.loads(response.text)
        except:
            # Logg when python dictionary convert process faill:
            RestCon.logger.warning("Python dictionary convert process faill.", self)
            jsonResponse = None

        # chech response status:
        if response.status_code < 200: # All respons from 0 to 199.
            RestCon.logger.warning("Connection to was a informational HTTPS.", self)
        elif response.status_code < 300: # All respons from 200 to 299.
            RestCon.logger.info("Connection to was a success HTTPS.", self)
        elif response.status_code < 400: # All respons from 300 to 399.
            RestCon.logger.warning("Connection to returned redirection HTTPS error.", self)
        elif response.status_code < 500: # All respons from 400 to 499.
            RestCon.logger.error("Connection to returned client HTTPS error.", self)
        elif response.status_code < 600: # All respons from 500 to 599.
            RestCon.logger.error("Connection to returned server HTTPS error.", self)
        # Return Https response in Json format:
        return jsonResponse

    def __responseToString(self, response) -> str:
        """
            __responseToString

            Parameters:
            -----------
            response: dict
                Description

            return:
            -------
            returnString: string
                Description
        """
        returnString = ""
        if isinstance(response, dict):
            for key in response:
                returnString = returnString + f"{key}: {response[key]}"
        return returnString