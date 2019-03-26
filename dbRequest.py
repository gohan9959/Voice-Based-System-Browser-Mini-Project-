#import win32api
import os
import sys
import createDB
def request():
    if(os.path.exists("Paths.db")):
        os.remove("Paths.db")
    #drives = win32api.GetLogicalDriveStrings()
    #a=drives.split("\000")
    #for i in range(0,len(a)-1):
        #if(a[i]!="C:\\"):
    print("Creating New Database!")
    createDB.create("C:\\test\\")