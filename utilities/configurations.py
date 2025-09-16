import configparser

def getconfig():
    config = configparser.ConfigParser()
    config.read("utilities/properties.ini")
    return config

def getPassword():
    return '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'