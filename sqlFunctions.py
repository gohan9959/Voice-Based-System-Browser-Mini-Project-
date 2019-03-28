import sqlite3 as sql
import os
import endMenu
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
    endMenu.eMenu()

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
    print("Closing Connection to Database!")
    conn.close()
    print("Closed Connection to Database!")
    endMenu.eMenu()