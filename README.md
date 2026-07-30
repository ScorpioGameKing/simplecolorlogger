# simplecolorlogger
A simple to use logger that provides colored console logging and log file creation

## How to Install

To install simplecolorlogger you can run the following command to download it through pip

`pip install simplecolorlogger`

## How to Use

Below is a small python program demonstrating all of the steps required to create and use a logger
as well as each of the included update methods.

```py
from simplecolorlogger import Logger

if __name__ == "__main__":

    logger: Logger = Logger(5) # Logging Level defaults 0 so either set here or with the method below
    # logger.update_logging_level(5) # [0: Disabled, 1: INFO, 2: WARNING, 3: CRITICAL, 4: ERROR, 5: DEBUG]

    # All optional settings can be set when creating a logger or through these funtions

    logger.update_msg_class_name("Test Class")  # Only needed if user wants specificity, defaults "Logger"
    logger.update_msg_method_name("Test Method") # Only needed if user wants specificity, defaults "log_message"
    
    # logger.update_file_logging(False)  # Whether to save a log file, defaults False
    # logger.update_log_date_stamping(True)  # Whether to append the date, defaults True
    # logger.update_log_time_stamping(True)  # Whether to append the time, defaults True
    # logger.update_log_compact_stamp(False) # True: [2026-07-27]-[08-00-00] False: 20260727-080000
    # logger.update_log_save_name("log") # Log file name, defaults "log"
    # logger.update_log_save_location("./logs") # Log file save location, defaults "./logs"
    # logger.update_msg_time_stamping(True) # Whether to append the time, defaults True

    # To use pass your message and the level it logs at. If File logging is enabled it
    # will also save the log to the log file
    logger.log_message("This is a test log", 1)
    logger.log_message("This is a test log", 2)
    logger.log_message("This is a test log", 3)
    logger.log_message("This is a test log", 4)
    logger.log_message("This is a test log", 5)

    # You can also explictly log to only a file by using the following
    logger.log_file("This is ONLY logged to a file", 1)
```

The output of this program is below (Color is not added to the text)

```
❯ python test.py 
[08:07:50] :: [INFO] | [Test Class : Test Method] -> This is a test log
[08:07:50] :: [WARNING] | [Test Class : Test Method] -> This is a test log
[08:07:50] :: [CRITICAL] | [Test Class : Test Method] -> This is a test log
[08:07:50] :: [ERROR] | [Test Class : Test Method] -> This is a test log
[08:07:50] :: [DEBUG] | [Test Class : Test Method] -> This is a test log
```
