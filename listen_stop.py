import os

input() # Stop until kill signal
print("***Shutdown Signal Received. Program is shutting down***")
pids = os.popen("fuser 9000/tcp").read().split()
print("Killing " + " ".split(pids))
os.popen('sudo kill ' + " ".split(pids))
exit()