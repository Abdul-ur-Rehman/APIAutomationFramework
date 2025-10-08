import configparser
import mysql.connector
from mysql.connector import Error



def getconfig():
    config = configparser.ConfigParser()
    config.read("utilities/properties.ini")
    return config


def getPassword():
    with open(r"C:\Users\sg\Downloads\secret_token.txt", "r") as token:
        github_token = token.read().strip()
        return github_token

# Configurations for database connection
connect_config = {
    "host" : getconfig()['SQL']['host'],
    "database" : getconfig()['SQL']['database'],
    "user" : getconfig()['SQL']['user'],
    "password" : getconfig()['SQL']['password']
}

def getConnection():
    try:
        conn = mysql.connector.connect(**connect_config)
        if conn.is_connected():
            print("Connection Successful!")
            return conn
    except Error as e:
        print(e)

def getQuery(query):

    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute(query)
    row = cursor.fetchone()
    conn.close()
    return row