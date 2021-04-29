import os
import time
import paramiko
from pynput.keyboard import Listener as keylistener

controller_ip = "172.20.10.3" # change to match the ip of the controlling device, this default works on Zac's IPhone
pi_ip = "172.20.10.2" # change to match the ip of the raspberry pi, this default works on Zac's IPhone only

port = 22
username = "pi"
password = "R0b0t1cs"
command = "nc -lk -p 9000 | python3 Network_FlightController.py | nc " + controller_ip + " 9001"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(pi_ip, port, username, password)
ssh.exec_command("cd ~/Desktop/SLES-Drone/;" + command)

port = "9000"

def sendletter(letter_to_send):
    os.popen("echo " + letter_to_send + "| ncat "+pi_ip+" "+port)

currentstate = "r"

def on_press(key):
    key = str(key).replace("'", "")
    global currentstate
    if key != currentstate and key != 'r' and currentstate == 'r':
        sendletter(key)
    currentstate = key
    if key == "p":
        ssh.exec_command("nc -l -p 9003 | python3 /home/pi/Desktop/SLES-Drone/listen_stop.py | nc "+controller_ip+ " 9001")
        ssh.close()
        os.popen("echo p | ncat "+pi_ip+" 9003")
        print("\n\nScript to read session shut down...")
        time.sleep(3)
        os.system("cls")
        return False

def on_release(key):
    global currentstate
    if currentstate != 'r':
        sendletter('r')
    currentstate = 'r'

# From pynput module; this Listener sends incorporates the last two functions and calls them when keys are pressed or released according to their names

with keylistener(on_press = on_press, on_release = on_release) as listener:
    listener.join()