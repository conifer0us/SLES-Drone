import os
import keyboard
import time
import paramiko

controller_ip = "172.20.10.9" # change to match the ip of the controlling device, this default works on Connor's iPhone only

host = "172.20.10.8" # change to match the ip of the raspberry pi, this default works on Connor's iPhone only
port = 22
username = "pi"
password = "R0b0t1cs"

command = "nc -lk -p 9000 | python3 Network_FlightController.py | nc " + controller_ip + " 9001"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, port, username, password)
ssh.exec_command("sudo su;git pull;cd ~/Desktop/SLES-Drone/;" + command)
ssh.close()

pi_ip = "172.20.10.8"
port = "9000"

def sendletter(letter_to_send):
    os.popen("echo " + letter_to_send + "| ncat "+pi_ip+" "+port)

while True:
    revert_default = True
    letter = keyboard.read_key()
    if letter:
        sendletter(letter)
        time.sleep(.15)
        revert_default = True
    elif not letter and revert_default:
        sendletter(" ")
        revert_default = False
    if letter == "p":
        break