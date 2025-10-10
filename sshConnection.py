import paramiko as paramiko
from utilities.configurations import *

# Start Connection
config = getconfig()

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=config['Server']['host'], port=config['Server']['port'], username=config['Server']['username'], password=config['Server']['password'])


# Run Commands

stdin, stdout, stderr = ssh.exec_command('ls -a')
print(stdout.readlines())

stdin, stdout, stderr = ssh.exec_command('cat demofile')
print(stdout.readlines())