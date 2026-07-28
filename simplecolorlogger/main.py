from colorama import Fore, Style, just_fix_windows_console
from time import gmtime, strftime
from datetime import datetime
from os import path, remove, makedirs
import sys

class Logger():
    """
    A simple to use logger that provides colored log messages.
    logging_level: int -> [0: Disabled, 1: INFO, 2: WARNING, 3: CRITICAL, 4: ERROR, 5: DEBUG]
    Used to set the maximum logging level to be used.
        default = 0
    file_logging: bool -> Enable/Disable writing log file 
        default = False
    msg_time_stamping: bool -> Enable/Disable prepending a timestamp to log messages
        default = True
    msg_class_name: str -> The class name for the logged message 
        default = "Logger"
    msg_method_name: str -> The method name for the logged message  
        default = "log_message"
    log_date_stamping: bool -> Enable/Disable appending a datestamp to log files 
        default = True
    log_time_stamping: bool -> Enable/Disable appending a timestamp to log files 
        default = True
    log_compact_stamp: bool -> Enable/Disable compact date and timestamps 
        default = False
    log_save_location: str -> A relative path to the location where logs are save
        default = "./logs"
    log_save_name: str -> The generic name for the written log files 
        default = "log"
    """
    
    _logging_level: int = 0
    _file_logging: bool = False
    _msg_time_stamping: bool = True
    _msg_class_name: str = "Logger"
    _msg_method_name: str = "log_message"
    _log_date_stamping: bool = True
    _log_time_stamping: bool = True
    _log_compact_stamp: bool = False
    _log_time: str = ""
    _log_save_location: str = "./logs"
    _log_save_name: str = "log"

    _lb: str = f"{Style.BRIGHT}{Fore.LIGHTCYAN_EX}[{Style.RESET_ALL}"
    _rb: str = f"{Style.BRIGHT}{Fore.LIGHTCYAN_EX}]{Style.RESET_ALL}"
    _col: str = f"{Style.BRIGHT}{Fore.LIGHTCYAN_EX} : {Style.RESET_ALL}"
    _bar: str = f"{Style.BRIGHT}{Fore.LIGHTCYAN_EX} | {Style.RESET_ALL}"
    _arw: str = f"{Style.BRIGHT}{Fore.LIGHTCYAN_EX} -> {Style.RESET_ALL}"
    _lv1: str = f"{_lb}{Style.BRIGHT}{Fore.LIGHTBLUE_EX}INFO{Style.RESET_ALL}{_rb}{_bar}"
    _lv2: str = f"{_lb}{Style.BRIGHT}{Fore.LIGHTRED_EX}WARNING{Style.RESET_ALL}{_rb}{_bar}"
    _lv3: str = f"{_lb}{Style.BRIGHT}{Fore.LIGHTYELLOW_EX}CRITICAL{Style.RESET_ALL}{_rb}{_bar}"
    _lv4: str = f"{_lb}{Style.BRIGHT}{Fore.RED}ERROR{Style.RESET_ALL}{_rb}{_bar}"
    _lv5: str = f"{_lb}{Style.BRIGHT}{Fore.MAGENTA}DEBUG{Style.RESET_ALL}{_rb}{_bar}"

    def __init__(
            self, 
            logging_level: int = 0, 
            file_logging: bool = False, 
            msg_time_stamping: bool = True,
            msg_class_name: str = "",
            msg_method_name: str = "",
            log_date_stamping: bool = True,
            log_time_stamping: bool = True, 
            log_compact_stamp: bool = False,
            log_save_location: str = "", 
            log_save_name: str = ""
            ) -> None:
        self._logging_level = logging_level
        self._file_logging = file_logging
        self._msg_time_stamping = msg_time_stamping
        if not msg_class_name == "": 
            self._msg_class_name = msg_class_name
        if not msg_method_name == "": 
            self._msg_method_name = msg_method_name
        self._log_date_stamping = log_date_stamping
        self._log_compact_stamp = log_compact_stamp
        self.update_log_time_stamping(log_time_stamping)
        if not log_save_location == "": 
            self._log_save_location = log_save_location
        if not log_save_name == "": 
            self._log_save_name = log_save_name
        just_fix_windows_console()

    def update_logging_level(self, logging_level: int) -> None:
        """
        Update the current maximum logging level
        """
        self._logging_level = logging_level

    def update_file_logging(self, file_logging: bool) -> None:
        """
        Update whether to save a log file
        """
        self._file_logging = file_logging

    def update_log_date_stamping(self, log_date_stamping: bool) -> None:
        """
        Update whether to append a datestamp to log files 
        """
        self._log_date_stamping = log_date_stamping

    def update_log_compact_stamp(self, log_compact_stamp: bool) -> None:
        """
        Update whether the date and timestamps are compact or expanded
        """
        self._log_date_stamping = log_compact_stamp
        self.update_log_time_stamping(self._log_time_stamping)
    
    def update_log_time_stamping(self, log_time_stamping: bool) -> None:
        """
        Update whether to append a timestamp to log files 
        """
        self._log_time_stamping = log_time_stamping
        if self._log_time_stamping:
            if self._log_compact_stamp:
                self._log_time = f"-{datetime.now().strftime("%I%M%S")}"
            else:
                self._log_time = f"-{datetime.now().strftime("[%I-%M-%S]")}"
        else:
            self._log_time = ""

    def update_msg_time_stamping(self, msg_time_stamping: bool) -> None:
        """
        Update whether to prepend a timestamp to logged message
        """
        self._msg_time_stamping = msg_time_stamping
    
    def update_msg_class_name(self, msg_class_name: str) -> None:
        """
        Update the logger's class name
        """
        self._msg_class_name = msg_class_name

    def update_msg_method_name(self, msg_method_name: str) -> None:
        """
        Update the logger's method name
        """
        self._msg_method_name = msg_method_name

    def update_log_save_location(self, log_save_location: str) -> None:
        """
        Update the relative path of the log file save location
        """
        self._log_save_location = log_save_location

    def update_log_save_name(self, log_save_name: str) -> None:
        """
        Update the log's generic name
        """
        self._log_save_name = log_save_name

    def log_message(self, text: str, level: int = 0) -> None:
        """
        Used to both print and write a log message to the console and a file.
        text: str -> The raw text to log 
            No Default
        level: int -> The log level of the message. 0 in this context uses the Logger's current maximum
            default: 0
        """
        if level == 0: 
            level: int = self._logging_level
        if level <= self._logging_level and not self._logging_level == 0:
            _base: str = f"{self._lb}{Style.BRIGHT}{Fore.LIGHTGREEN_EX}{self._msg_class_name}{Style.RESET_ALL}{self._col}{Style.BRIGHT}{Fore.LIGHTWHITE_EX}{self._msg_method_name}{Style.RESET_ALL}{self._rb}{self._arw}{text}"
            _msg_stamp: str = ""
            if self._msg_time_stamping: 
                _msg_stamp: str = f"{datetime.now().strftime("[%I:%M:%S] :: ")}"
            match level:
                case 1:
                    sys.stdout.write(f"{_msg_stamp}{self._lv1}{_base}\n")
                case 2:
                    sys.stdout.write(f"{_msg_stamp}{self._lv2}{_base}\n")
                case 3:
                    sys.stdout.write(f"{_msg_stamp}{self._lv3}{_base}\n")
                case 4:
                    sys.stdout.write(f"{_msg_stamp}{self._lv4}{_base}\n")
                case 5:
                    sys.stdout.write(f"{_msg_stamp}{self._lv5}{_base}\n")
                case _:
                    sys.stdout.write(f"{_msg_stamp}{self._lv1}{_base}\n")
            if self._file_logging:
                _file_stamp = "" 
                if self._log_date_stamping:
                    if self._log_compact_stamp:
                        _file_stamp: str = f"-{strftime("%Y%m%d", gmtime())}"
                    else:
                        _file_stamp: str = f"-{strftime("[%Y-%m-%d]", gmtime())}"
                if path.exists(f"{self._log_save_location}/"):
                    if path.exists(f"{self._log_save_location}/{self._log_save_location}{_file_stamp}{self._log_time}"): 
                        remove(f"{self._log_save_location}/{self._log_save_location}{_file_stamp}{self._log_time}")
                else:
                    makedirs(f"{self._log_save_location}/")
                with open(f"{self._log_save_location}/{self._log_save_name}{_file_stamp}{self._log_time}", "a") as log_file:
                    match level:
                        case 1:
                            log_file.write(f"{_msg_stamp}[INFO] | [{self._msg_class_name} : {self._msg_method_name}] -> {text}\n")
                        case 2:
                            log_file.write(f"{_msg_stamp}[WARNING] | [{self._msg_class_name} : {self._msg_method_name}] -> {text}\n")
                        case 3:
                            log_file.write(f"{_msg_stamp}[CRITICAL] | [{self._msg_class_name} : {self._msg_method_name}] -> {text}\n")
                        case 4:
                            log_file.write(f"{_msg_stamp}[ERROR] | [{self._msg_class_name} : {self._msg_method_name}] -> {text}\n")
                        case 5:
                            log_file.write(f"{_msg_stamp}[DEBUG] | [{self._msg_class_name} : {self._msg_method_name}] -> {text}\n")
                        case _:
                            log_file.write(f"{_msg_stamp}[INFO] | [{self._msg_class_name} : {self._msg_method_name}] -> {text}\n")
