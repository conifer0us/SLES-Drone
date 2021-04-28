import os

input() # Stop until kill signal
print("***Shutdown Signal Received. Program is shutting down***")
os.popen("fuser -k 9000/tcp")
exit()