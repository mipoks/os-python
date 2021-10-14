import os
import sys
import random
import time

# Coded By Daniyar Zakiev. Group 11-902
if (len(sys.argv) != 2):
    print("You should enter time for sleeping!");
    os._exit(1);

print("Hello from child process [PID=%d] with sleeping time=%d" % (os.getpid(), int(sys.argv[1])));
time.sleep(int(sys.argv[1]));
print("Bye from child process [PID=%d]!" % (os.getpid()));
os._exit(random.randint(0, 1));
