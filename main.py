import os
import dbRequest
import menu
import forBrowser
if(not os.path.exists("Path.db")):
    forBrowser.createBrowserList()
if(not os.path.exists("Paths.db")):
    dbRequest.request()
menu.options()