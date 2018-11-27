import os
import time
import sys

try:
    while True:
        comnd=input("enter your command:")
        os.system(comnd)
        time.sleep(2)
expect:
    KeyboardInterrupt()
    sys.exit()
