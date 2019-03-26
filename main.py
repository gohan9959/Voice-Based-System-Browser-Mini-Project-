import os
import dbRequest
import menu
if(not os.path.exists("Paths.db")):
    dbRequest.request()
menu.options()