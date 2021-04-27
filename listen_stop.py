import os

def killall():    
    pids = os.popen("sudo fuser 9000/tcp").read().replace("  "," ").split(" ")
    pids.remove("")
    for pid in pids:
        os.popen('sudo kill ' + pid)

os.popen("echo Listen_stop activated and will shut program down when p is pressed. | nc 172.20.10.9 9001")
input() # Stop until kill signal
killall()
os.popen("echo ***Shutdown Signal Received. Program is shutting down*** | nc 172.20.10.9 9001")
exit()