import os
import time
import paramiko
import msvcrt

controller_ip = "172.20.10.3" # change to match the ip of the controlling device, this default works on Zac's IPhone

host = "172.20.10.2" # change to match the ip of the raspberry pi, this default works on Zac's IPhone only
port = 22
username = "pi"
password = "R0b0t1cs"

command = "nc -lk -p 9000 | python3 Network_FlightController.py | nc " + controller_ip + " 9001"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, port, username, password)
ssh.exec_command("cd ~/Desktop/SLES-Drone/;" + command)

port = "9000"

def sendletter(letter_to_send):
    os.popen("echo " + letter_to_send + "| ncat "+host+" "+port)

while True:
    try:
        if msvcrt.kbhit():
            while msvcrt.kbhit():
                letter = msvcrt.getwche()
                if letter != "r": sendletter(letter)
                if letter == "p": 
                    ssh.exec_command("nc -l 9003 | python3 /home/pi/Desktop/SLES-Drone/listen_stop.py")
                    ssh.close()
                    os.popen("echo p | ncat "+host+" 9003")
                    raise EnvironmentError
                time.sleep(.25)
            sendletter("r")
    except:
        break