#!/usr/bin/env python3
# @file     logger.py
# @brief    Logging system class
# Daryl Dang - 2021

###########
# IMPORTS #
###########
import logging
from enum import IntEnum, auto

#############
# CONSTANTS #
#############
LOGGING_FILE_NAME = "log.log"

###########
# GLOBALS #
###########

#####################
# Class Definitions #
#####################
class VerbosityLevel(IntEnum):
    """
    Enum for verbosity levels.
    """
    VERBOSITY_LEVEL0 = 0        # No logs or prints
    VERBOSITY_LEVEL1 = auto()   # Critical/errors/warnings levels and prints to console
    VERBOSITY_LEVEL2 = auto()   # Info/debug level and prints to console

class Logger:
    """
    Singleton class of the logger system that will handle the logging system of the game.
    ...

    Attributes
    ----------
    _logger_instance: Logger
        Represents the current running instance of Logger, this will only be created once (by default set to None).
    _verbosity_level: int
        Represents the verbosity level (by default set to VERBOSITY_LEVEL0).
    _print_statements_enabled : bool
        Represents if print statements are going to be enabled (by default set to False).
    """
    _logger_instance = None
    _verbosity_level = int(VerbosityLevel.VERBOSITY_LEVEL0)
    _print_statements_enabled = False

    @staticmethod
    def get_instance():
        """
        Obtains instance of Logger.
        """
        if Logger._logger_instance is None:
            Logger()
        return Logger._logger_instance

    def __init__(self) -> None:
        """
        Default constructor.
        """
        if Logger._logger_instance != None:
            raise Exception("{}: Cannot construct, an instance is already running.".format(__file__))
        else:
            Logger._logger_instance = self

    def set_print_statements(self, print_flag: bool) -> None:
        """
        Sets if print statements will enabled/disabled.

        Args:
            print_flag (bool): Boolean flag to enable/disable print statements.
        """
        if print_flag:
            self._print_statements_enabled = print_flag
        else:
            self._print_statements_enabled = print_flag

    def set_verbosity_level(self, verbosity_level: int) -> bool:
        """
        Sets the verbosity level of logger.

        Args:
            verbosity_level (int): Level of verbosity that will be set to logger.

        Returns:
            bool: Returns if verbosity level was set successfully.
        """
        _enum_values = [item.value for item in VerbosityLevel]
        if verbosity_level in _enum_values:
            # Set verbosity level
            self._verbosity_level = verbosity_level

            # Switcher
            _switch = {
                0: self._set_verbosity_level0,
                1: self._set_verbosity_level1,
                2: self._set_verbosity_level2
                }

            # Set logging level based on verbosity set
            _switch.get(verbosity_level, None)()

            return True
        else:
            return False

    def _set_verbosity_level0(self):
        """
        Set verbosity level 0.
        """
        pass

    def _set_verbosity_level1(self):
        """
        Set verbosity level 1.
        """
        logging.basicConfig( filename=LOGGING_FILE_NAME, \
                             filemode='w', \
                             format='%(asctime)s - %(levelname)s \t- %(message)s', \
                             level=logging.WARNING )

    def _set_verbosity_level2(self):
        """
        Set verbosity level 2.
        """
        logging.basicConfig( filename=LOGGING_FILE_NAME, \
                             filemode='w', \
                             format='%(asctime)s - %(levelname)s \t- %(message)s', \
                             level=logging.DEBUG )

    def print_critical(self, message: str="", src_file: str="") -> None:
        """
        Prints and logs critical to console if verbosity level 1 or more set.

        Args:
            message (str, optional)     : Message to print to console. Defaults to "".
            src_file (str, optional)    : [description]. Defaults to "".
        """
        if self._verbosity_level >= int(VerbosityLevel.VERBOSITY_LEVEL1):
            _mes = src_file + ": " + message
            if self._print_statements_enabled:
                print("CRITICAL \t- ", src_file + ": \t" + message)
            logging.critical(_mes)

    def print_error(self, message: str="", src_file: str="") -> None:
        """
        Prints and logs error to console if verbosity level 1 or more set.

        Args:
            message (str, optional)     : Message to print to console. Defaults to "".
            src_file (str, optional)    : [description]. Defaults to "".
        """
        if self._verbosity_level >= int(VerbosityLevel.VERBOSITY_LEVEL1):
            _mes = src_file + ": " + message
            if self._print_statements_enabled:
                print("ERROR \t\t- ", src_file + ": \t" + message)
            logging.error(_mes)

    def print_warning(self, message: str="", src_file: str="") -> None:
        """
        Prints and logs warning to console if verbosity level 1 or more set.

        Args:
            message (str, optional)     : Message to print to console. Defaults to "".
            src_file (str, optional)    : [description]. Defaults to "".
        """
        if self._verbosity_level >= int(VerbosityLevel.VERBOSITY_LEVEL1):
            _mes = src_file + ": " + message
            if self._print_statements_enabled:
                print("WARNING \t- ", src_file + ": \t" + message)
            logging.warning(_mes)

    def print_info(self, message: str="", src_file: str="") -> None:
        """
        Prints and logs info to console if verbosity level 2 or more set.

        Args:
            message (str, optional)     : Message to print to console. Defaults to "".
            src_file (str, optional)    : [description]. Defaults to "".
        """
        if self._verbosity_level >= int(VerbosityLevel.VERBOSITY_LEVEL2):
            _mes = src_file + ": " + message
            if self._print_statements_enabled:
                print("INFO \t\t- ", src_file + ": \t" + message)
            logging.info(_mes)

    def print_debug(self, message: str="", src_file: str="") -> None:
        """
        Prints and logs debug to console if verbosity level 2 or more set.

        Args:
            message (str, optional)     : Message to print to console. Defaults to "".
            src_file (str, optional)    : [description]. Defaults to "".
        """
        if self._verbosity_level >= int(VerbosityLevel.VERBOSITY_LEVEL2):
            _mes = src_file + ": " + message
            if self._print_statements_enabled:
                print("DEBUG \t\t- ", src_file + ": \t" + message)
            logging.debug(_mes)