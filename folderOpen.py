import win32api
import os
import sys
import threading
import search as s
def op(request):
    #drives = win32api.GetLogicalDriveStrings()
    #a=drives.split("\000")
    #for i in range(0,len(a)-1):
        #if(a[i]!="C:\\"):
            s.srch("C:\\test\\",request)
        
        
    
        
