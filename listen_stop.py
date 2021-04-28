import os
import subprocess
import time

input() # Stop until kill signal
print("***Shutdown Signal Received. Program is shutting down***")
time.sleep(.25)
pids = subprocess.check_output("fuser 9000/tcp").split()
for pid in pids:
    print("Killing " + pid)
    os.popen('sudo kill ' + pid)
exit()