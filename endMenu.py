import menu
import voiceParse as vp
def eMenu():
    qry = str()            
    print("1.Menu\n2.Exit\nYour Choice:")
    qry=vp.query("2")
    if(qry == '1' or "menu" in qry.lower()):
        menu.options()
    elif(qry == '2' or "exit" in qry.lower()):
        print("Bye!!")
    else:
        print("Wrong Choice!!")
        eMenu()