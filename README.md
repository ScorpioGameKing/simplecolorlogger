# simplecolorlogger
A simple to use logger that provides colored console logging and log file creation

## How to Install

To install simplecolorlogger you can run the following command to download it through pip

`pip install simplecolorlogger`

## How to Use

Import the package as follows, it only provides one class.

`from simplecolorlogger import Logger`

Once imported you will need to create an instance of the logger. When creating the 
logger you can provide the following values to configure it:

    - logging_level: int -> [0: Disabled, 1: INFO, 2: WARNING, 3: CRITICAL, 4: ERROR, 5: DEBUG]
        - Used to set the maximum logging level to be used.
        - default = 0
    - file_logging: bool
        - Enable/Disable writing log file 
        - default = False
    - log_save_location: str
        - A relative path to the location where logs are save
        - default = "./logs"
    - log_save_name: str
        - The generic name for the written log files 
        - default = "log"
    - log_time_stamping: bool
        - Enable/Disable appending a datestamp to log files 
        - default = True
    - msg_time_stamping: bool
        - Enable/Disable prepending a timestamp to log messages
        - default = True

Once the logger has been setup you can simply call `logger.log_message()`. You will need to at 
minimum provide the raw text to log. The full option list is as follows:

    - text: str
        - The raw text to log 
        - No Default
    - level: int
        - The log level of the message. 0 in this context uses the Logger's current maxium
        - default: 0
    - class_name: str
        - The name of the class the log is being sent from
        - default: "Logger"
    - method_name: str
        - The name of the method the log is being sent from
        - default: "log_message"

There are several helper methods also provided for updating the logger options. Each follows
the same naming convention of `update_{option}(new_option_value)`, replacing `{option}` with 
the option's name i.e `update_file_logging(True)`