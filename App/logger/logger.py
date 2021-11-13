# Python Imports:
import os
from typing import Tuple

# Application Imports:
from .models import LoggerData, AdditionalData

# Severity constants declaration:
FULLDEBUG = 0
DEBUG = 1
INFO = 2
WARNING = 3
ERROR = 4
CRITICAL = 5


class Logger():

    def __init__(self, application: str = 'NoName') -> None:
        self.application = application

    def debug(self, message: str, module: str = None, additional_data: dict = False) -> Tuple:
        """
            Create a new log based on the following data:

                Method attributes:
                -----------------
                message: string
                    Logging message string value. 
                module: string
                    Module or function name.
                additional_data: dict
                    Optional data in dict format, added to AdditionalData models.
        """
        return self.__log(DEBUG, message, module, additional_data)

    def info(self, message: str, module: str = None, additional_data: dict = False) -> Tuple:
        """
            Create a new log based on the following data:

                Method attributes:
                -----------------
                message: string
                    Logging message string value. 
                module: string
                    Module or function name.
                additional_data: dict
                    Optional data in dict format, added to AdditionalData models.
        """
        return self.__log(INFO, message, module, additional_data)


    def warning(self, message: str, module: str = None, additional_data: dict = False) -> Tuple:
        """
            Create a new log based on the following data:

                Method attributes:
                -----------------
                message: string
                    Logging message string value. 
                module: string
                    Module or function name.
                additional_data: dict
                    Optional data in dict format, added to AdditionalData models.
        """
        return self.__log(WARNING, message, module, additional_data)


    def error(self, message: str, module: str = None, additional_data: dict = False) -> Tuple:
        """
            Create a new log based on the following data:

                Method attributes:
                -----------------
                message: string
                    Logging message string value. 
                module: string
                    Module or function name.
                additional_data: dict
                    Optional data in dict format, added to AdditionalData models.
        """
        return self.__log(ERROR, message, module, additional_data)

    def critical(self, message: str, module: str = None, additional_data: dict = False) -> Tuple:
        """
            Create a new log based on the following data:

                Method attributes:
                -----------------
                message: string
                    Logging message string value. 
                module: string
                    Module or function name.
                additional_data: dict
                    Optional data in dict format, added to AdditionalData models.
        """
        return self.__log(CRITICAL, message, module, additional_data)

    def __log(self, severity, message: str, module: str, additional_data: dict) -> Tuple:
        """ Create new log in Database """
        new_log = None
        new_additional_data = None

        new_log = LoggerData.objects.create(
            process = os.getpid(),
            application = str(self.application),
            module = str(module),
            severity = severity,
            message = str(message),
        )

        if additional_data is not False:
            for data in additional_data:
                new_additional_data = AdditionalData.objects.create(
                    name = data,
                    value = additional_data[data],
                    logger = new_log,
                )
            
        return (new_log, new_additional_data)