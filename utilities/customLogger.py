import logging


# This is logging class
class LogGen:

    # Define the logger for generate logs during execution
    @staticmethod
    def loggen():
        logger = logging.getLogger(__name__)
        filehandler = logging.FileHandler('.\\logs\\logging.log')

        formatter = logging.Formatter("%(asctime)s: %(levelname)s: %(name)s: %(message)s")

        filehandler.setFormatter(formatter)

        logger.addHandler(filehandler)

        logger.setLevel(logging.INFO)

        return logger
