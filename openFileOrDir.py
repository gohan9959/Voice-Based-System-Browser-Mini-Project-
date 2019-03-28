import os
import prettytable as pt
import voiceParse as vp
def open(request = [[]], op = int):
    if(len(request)==1):
        exactOrSimilar(op)
        try:
            print("Opening Request!")
            os.startfile(request[0][1])
        except:
            print("This Project Does not Support Executable Files Yet!")
        else:
            print("Opened Requested Query!")
            return op
    elif(len(request)>1):
        exactOrSimilar(op+2)
        multipleOptions(request,op)
    else:
        op = -1
        exactOrSimilar(op)
        return op

def multipleOptions(request = [[]],op = int):
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
        except:
            print("This Project Does not Support Executable Files Yet!")
        else:
            print("Opened Requested Query!")
            return op
    else:
        print("Invalid Option!")
        multipleOptions(request)

def exactOrSimilar(op):
    if(op == 0):
        print("Found Requested Query!")
    elif(op == 1):
        print("Found Similar Query!")
    elif(op == 2):
        print("Found Multiple Queries For Requested Query!")
    elif(op == 3):
        print("Found Multiple Similar Queries!")
    elif(op == -1):
        print("Requested Query Not Found!")