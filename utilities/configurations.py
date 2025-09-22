import configparser

def getconfig():
    config = configparser.ConfigParser()
    config.read("utilities/properties.ini")
    return config

def getPassword():
    with open(r"C:\Users\sg\Downloads\secret_token.txt", "r") as token:
        github_token = token.read().strip()
        return github_token
