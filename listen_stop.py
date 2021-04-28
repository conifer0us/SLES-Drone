import os

input() # Stop until kill signal
print("***Shutdown Signal Received. Program is shutting down***")
pids = os.popen("sudo fuser 9000/tcp").read().replace("  "," ").split()
for pid in pids:
    print("Killing " + pid)
    os.popen('sudo kill ' + pid)
exit()