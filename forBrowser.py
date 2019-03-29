import sqlite3 as sql
import os
import win32api as w32
import prettytable as pt
import voiceParse as vp
import endMenu
def createBrowserList():
        winDrive=w32.GetWindowsDirectory().split(':')[0]
        conn=sql.connect('Path.db')
        conn.execute('''CREATE TABLE IF NOT EXISTS DEFBROWSER(NAME VARCHAR(200),PATH VARCAR(1000),DEF INT);''')
        browsers=[['Chrome',winDrive+':\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe'],['Firefox',winDrive+':\\Program Files\\Mozilla Firefox\\firefox.exe'],['Opera',winDrive+':\\Users\\'+os.getenv('username')+'\\AppData\\Local\\Programs\\Opera\\Opera.exe'],['Opera',winDrive+':\\Program Files\\Opera'],['Microsoft Edge',winDrive+':\\Windows\\SystemApps\\Microsoft.MicrosoftEdge_8wekyb3d8bbwe\\MicrosoftEdge.exe']]
        for i in range(len(browsers)):
                conn.execute('''INSERT INTO DEFBROWSER VALUES(?,?,?)''',(browsers[i][0],browsers[i][1],'0'))
        print("Created Browser List")
        conn.commit()
def setDefaultBrowser():
        print("Select Default Browser To Open URLs")
        conn=sql.connect('Path.db')
        cur=conn.cursor()
        values=cur.execute('''SELECT * FROM DEFBROWSER''')
        val=values.fetchall()
        print(val)
        table=pt.PrettyTable(["Option","Name"])
        for i in range(len(val)):
                if(os.path.exists(val[i][1])):
                        table.add_row([i+1,val[i][0]])
        print("Select Option Number From Below!")
        print(table)
        req=vp.query("4")
        try:
                req=int(req)
        except:
                print("Give Option In Numbers Only")
                req=-1
        if (req>0 and req<=len(val)+1):
                cur.execute('''UPDATE DEFBROWSER SET DEF = 0 WHERE DEF = 1''')
                rqst=(val[req-1][0],)
                cur.execute('''UPDATE DEFBROWSER SET DEF = 1 WHERE NAME = ?''',rqst)
                values=cur.execute('''SELECT * FROM DEFBROWSER''')
                val=values.fetchall()
                print(val)
                conn.commit()
        else:
                print("Invalid Option!")
                setDefaultBrowser()
        endMenu.eMenu()