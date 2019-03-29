import webbrowser as wb
import endMenu
import os
import sqlite3 as sql
def open(request):
    conn=sql.connect('Path.db')
    cur=conn.cursor()
    pth=cur.execute('''SELECT * FROM DEFBROWSER WHERE DEF = 1''')
    path1=pth.fetchone()
    path=path1[1].replace('\\','/')+' %s'
    print("Opening URL!")
    try: 
        wb.get(path).open_new_tab(request)
    except:
        try:
            wb.open_new_tab(request)
        except:
            print("Unable To Open URL!")
        else:
            print("URL Opened!")
    else:
        print("URL Opened!")
    endMenu.eMenu()
