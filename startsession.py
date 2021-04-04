import os
import keyboard
import time
import paramiko

controller_ip = "" # change to match the ip of the controlling device

host = "" # change to match the ip of the raspberry pi
port = 22
username = "pi"
password = "r0b0t1cs"

command = "nc -lk -p 9000 | python3 Network_FlightController.py | nc " + controller_ip + " 9001"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, port, username, password)
ssh.exec_command("sudo su;git pull;cd ~/Desktop/SLES-Drone/;" + command)
ssh.close()

pi_ip = input("What is the ip of the device that is receiving this keyboard input? (Default localhost)    ")
port = input("What port do you want to connect to? (Default 9000)    ")
if pi_ip == "": pi_ip = "127.0.0.1"
if port == "": port = "9000"

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