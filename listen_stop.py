import os

def killall():    
    pids = os.popen("fuser 9000/tcp").read().replace("  "," ").split(" ")
    pids.remove("")
    for i in pids:
        os.popen('kill ' + i)

os.popen("echo \nListen_stop activated and will shut program down when p is pressed. | nc 172.20.10.9 9001")

while True:
    shutdown = input().replace("\n", "")[0]
    if shutdown == "p":
        killall()
        os.popen("echo \n\n \*\*\*Shutdown Signal Received. Program is shutting down\*\*\* | nc 172.20.10.9 9001")
        exit()