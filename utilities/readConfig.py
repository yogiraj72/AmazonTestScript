import configparser

# This class is used to read the configuration file config.ini
config = configparser.RawConfigParser()

config.read(".\\Configuration\\config.ini")


class ReadConfig:
    @staticmethod
    def getappurl():
        url = config.get('common info', 'baseUrl')
        return url

    @staticmethod
    def searchword():
        search = config.get('common info', 'searchWord')
        return search

    @staticmethod
    def minvalue():
        minval = config.get('common info', 'minValue')
        return minval

    @staticmethod
    def maxvalue():
        maxval = config.get('common info', 'maxValue')
        return maxval

