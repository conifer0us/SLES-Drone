import os

def killall():    
    pids = os.popen("fuser 9000/tcp").read().replace("  "," ").split(" ")
    for i in pids:
        if i:
            os.popen('kill ' + i)

os.popen("echo listen_stop activated and will shut program down when p is pressed. | nc 172.20.10.9 9001")

while True:
    shutdown = input().replace("\n", "")[0]
    if shutdown == "p":
        killall()
        exit()