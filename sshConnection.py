import paramiko as paramiko
from utilities.configurations import *

# Start Connection

ssh = getSSHConnection()

# Run Commands

stdin, stdout, stderr = ssh.exec_command('ls -a')
print(stdout.readlines())

stdin, stdout, stderr = ssh.exec_command('cat demofile')
print(stdout.readlines())

#Upload CSV
source = "batchFiles/loanasa.csv"
destination = "loanasa.csv"

uploadFile(source, destination)

#Upload .py
source = "batchFiles/script.py"
destination = "script.py"
uploadFile(source, destination)

stdin, stdout, stderr = ssh.exec_command('ls -a')
print(stdout.readlines())

ssh.close()