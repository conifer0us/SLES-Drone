import os
import sys
import time
import keyboard
import msvcrt

pi_ip = input("What is the ip of the device that is receiving this keyboard input? (Default localhost)    ")
port = input("What port do you want to connect to?(Default 4206)    ")
if pi_ip == "": pi_ip = "127.0.0.1"
if port == "": port = "9000"

def sendletter(letter_to_send):
    os.popen("echo " + letter_to_send + "| ncat "+pi_ip+" -4 -p "+port)

while True:
    if msvcrt.kbhit():
        sendletter(msvcrt.getch().decode('utf-8'))
        if msvcrt.getch().decode('utf-8') == "p":
            break
        time.sleep(.5)