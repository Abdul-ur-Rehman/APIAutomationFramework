from utilities.configurations import *
import csv

# Start Connection

ssh = getSSHConnection()

# Run Commands

stdin, stdout, stderr = ssh.exec_command('ls -a')
print(stdout.readlines())

stdin, stdout, stderr = ssh.exec_command('cat demofile')
print(stdout.readlines())

#Uploading CSV File
source = "batchFiles/loanasa.csv"
destination = "loanasa.csv"

uploadFile(source, destination)

#Uploading .py File
source = "batchFiles/script.py"
destination = "script.py"
uploadFile(source, destination)

stdin, stdout, stderr = ssh.exec_command('ls -a')
print(stdout.readlines())

#Executing batch commands on remote server
stdin, stdout, stderr = ssh.exec_command("python3 script.py")


#Downloading File
source = "loanasa.csv"
destination = "outputFiles/loanasa.csv"
downloadFile(source,destination)

#Parsing output csv file
with open("outputFiles/loanasa.csv") as csvFile:
    csvReader = csv.reader(csvFile, delimiter= ",")
    for row in csvReader:
        if row[0] == "43243":
            assert row[1] == "approved"

#Removing files from server
stdin, stdout, stderr = ssh.exec_command('rm -f loanasa.csv script.py')

ssh.close()