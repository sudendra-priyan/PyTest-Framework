import inspect
import logging


def customLogger(logLevel=logging.DEBUG):

    # Gets the name of the class/ method where this method is called
    loggerName = inspect.stack()[1][3]
    logger = logging.getLogger(loggerName)

    # Setting the level of log required
    logger.setLevel(logging.DEBUG)

    # Naming the Log file which is going to be generated
    fileHandler = logging.FileHandler("Automation.log", mode="w")
    fileHandler.setLevel(logLevel)

    # Format of the lgo file
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s',
                                  datefmt='%m/%d/%Y %I:%M:%S %p')

    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)

    return logger
