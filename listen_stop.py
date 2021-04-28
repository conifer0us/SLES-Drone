import os

input() # Stop until kill signal
print("***Shutdown Signal Received. Program is shutting down***")
os.system("sudo fuser -k 9000/tcp")
exit()