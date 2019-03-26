import os
import prettytable as pt
import voiceParse as vp
def open(request = [[]], op = int):
    if(len(request)==1):
        try:
            print("Opening Request!")
            os.startfile(request[0][1])
            print("Opened Requested Query!")
        except:
            print("This Project Does not Support Executable Files Yet!")
        return 1+op
    elif(len(request)>1):
        multipleOptions(request)
        return 1+op
    else:
        return -1

def multipleOptions(request = [[]]):
    table=pt.PrettyTable(["Option","Name","Path"])
    for i in range(len(request)):
        table.add_row([i+1,request[i][0],request[i][1]])
    print("Select Option Number From Below!")
    print(table)
    print("Your Option:")
    req=vp.query("3")
    try:
       req=int(req)
    except:
        print("Give Option Numbes Only")
        req=-1
    if (req>0 and req<=len(request)+1):
        try:
            print("Opening Request!")
            os.startfile(request[req-1][1])
            print("Opened Requested Query!")
        except:
            print("This Project Does not Support Executable Files Yet!")
    else:
        print("Invalid Option!")
        multipleOptions(request)