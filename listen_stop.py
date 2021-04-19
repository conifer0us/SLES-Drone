import os

pids = os.popen("fuser 9000/tcp").read().replace("  "," ").split(" ").remove('')
for i in pids:
    os.popen('kill ' + i)