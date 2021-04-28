import os

input() # Stop until kill signal
print("***Shutdown Signal Received. Program is shutting down***")
pids = os.system("fuser 9000/tcp").read().split()
print("Killing " + " ".join(pids))
os.popen('sudo kill ' + " ".join(pids))
exit()