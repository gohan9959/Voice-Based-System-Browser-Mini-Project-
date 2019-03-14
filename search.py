import os
import sys
import time
import subprocess
def srch(drives,request):
    f=-1
    for root, dirs, files in os.walk(drives,topdown=True):
                for name in files:
                    path=os.path.join(root, name)
                    print(path)
                    s1=path.split("\\")
                    s11=s11=s1[len(s1)-1].split(".")
                    s2=path.split(":")
                    s22=s2[len(s2)-1].split(".")
                    if(request.lower()==s11[0].lower() or request.lower()==s22[0]):
                        print("Found File opening...")
                        time.sleep(3)
                        os.startfile(path)
                        print("Opened!")
                        time.sleep(5)
                        f=1
                        break
                    
                for name in dirs:
                    path=os.path.join(root, name)
                    print(path)
                    s1=path.split("\\")
                    s2=path.split(":")
                    if(request.lower()==s1[len(s1)-1].lower() or request.lower()==s2[len(s2)-1].lower()):
                        print("Found Directory opening...")
                        time.sleep(3)
                        os.startfile(path)
                        print("Opened!")
                        time.sleep(5)
                        f=1
                        break
                if(f==1):
                    break

    if(f==-1):
        print("File or Folder not found")
        time.sleep(5)
