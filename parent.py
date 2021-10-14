import os
import sys
import random
import time

# Coded By Daniyar Zakiev. Group 11-902
if (len(sys.argv[1]) != 2):
    print("You should enter number of process!");
    os._exit(1);

N = int(sys.argv[1]);
for i in range (0, N):
    info = os.fork();
    if (info == 0):
        sleeping_time = random.randint(5, 10);
        os.execv(sys.executable, ("python3", "./child.py", str(sleeping_time));
for i in range (0, N):
    ans = os.wait();
    print("Child process [PID=%d] with status %d finished." % (ans[0], ans[1]));