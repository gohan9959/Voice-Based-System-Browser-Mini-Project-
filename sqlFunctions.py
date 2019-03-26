import sqlite3 as sql
import os
import menu
import voiceParse as vp
import openFileOrDir as ofd
def putValues(names = [],paths = []):
    print("Connecting to Database!")
    conn = sql.connect("Paths.db")
    print("Connected to Database!")
    conn.execute('''CREATE TABLE IF NOT EXISTS SYSDIR(NAME VARCHAR(200),PATH VARCAR(1000));''')
    print("Inserting Paths into Database!")
    for name,path in zip(names,paths):
        print("Inserting:"+name+" "+path+"!")
        conn.execute('''INSERT INTO SYSDIR VALUES(?,?)''',(name,path))
        print("Inserted:"+name+" "+path+"!")
    print("Saving Database!")
    conn.commit()
    print("Database Saved!")
    print("Closing Connection to Database!")
    conn.close()
    print("Closed Connection to Database!")
    endMenu()

def getValues(request):
    print("Connecting to Database!")
    conn = sql.connect("Paths.db")
    print("Connected to Database!")
    print("Searching for Requested Query!")
    cur=conn.cursor()
    rqst=(request,)
    values=cur.execute('''SELECT * FROM SYSDIR WHERE NAME = ?''',rqst)
    val=values.fetchall()
    flag=ofd.open(val,0)
    if(flag == -1):
        rqst=('%'+request+'%',)
        values=cur.execute('''SELECT * FROM SYSDIR WHERE NAME LIKE ?''',rqst)
        val=values.fetchall()
        flag=ofd.open(val,1)
    if(flag == 1):
        print("Found Requested Query!")
    elif(flag == 2):
        print("Found Similar Query!")
    else:
        print("Requested Query Not Found!")
    print("Closing Connection to Database!")
    conn.close()
    print("Closed Connection to Database!")
    endMenu()

def endMenu():            
    print("1.Menu\n2.Exit\nYour Choice:")
    qry=vp.query("2")
    if(qry == '1' or qry.lower() == "menu"):
        menu.options()
    elif(qry == '2' or qry.lower() == "exit"):
        print("Bye!!")
    else:
        print("Wrong Choice!!")
        endMenu()