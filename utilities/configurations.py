import configparser
import mysql.connector
from mysql.connector import Error
import paramiko as paramiko



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

def getSSHConnection():
    config = getconfig()
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    host = config['Server']['host']
    port = config['Server']['port']
    username = config['Server']['username']
    password = password=config['Server']['password']
    ssh.connect(hostname= host, port= port, username= username, password= password)

    return ssh

def uploadFile(source, destination):
    ssh = getSSHConnection()
    sftp = ssh.open_sftp()
    sftp.put(source, destination)