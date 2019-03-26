import os
import sys
import time
import sqlFunctions as sfun
import re
def create(drives):
    drives="C:\\test\\"
    names = []
    paths = []
    for root, dirs, files in os.walk(drives,topdown=True):
        for name in files:
            path=os.path.join(root, name)
            fname = [re.sub(r"[^a-zA-Z0-9]+", ' ', k) for k in name.split("\n")]
            name=fname[0].rsplit(' ', 1)[0]
            names.append(name.lower())
            paths.append(path) 
        for name in dirs:
            path=os.path.join(root, name)
            fname = [re.sub(r"[^a-zA-Z0-9]+", ' ', k) for k in name.split("\n")]
            name=fname[0]
            names.append(name.lower())
            paths.append(path)
    sfun.putValues(names,paths)