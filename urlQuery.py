import webbrowser as wb
import endMenu
import os
def open(request):
    cpath='C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe'
    fpath='C:\\Program Files\\Mozilla Firefox\\firefox.exe'
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    firefox_path= 'C:/Program Files/Mozilla Firefox/firefox.exe %s'
    print("Opening URL!") 
    if(os.path.exists(cpath)):
        wb.get(chrome_path).open_new_tab(request)
    elif(os.path.exists(fpath)):
        wb.get(firefox_path).open_new_tab(request)
    else:
        try:
            wb.open_new_tab(request)
        except:
            print("Unable To Open URL!")
        else:
            print("URL Opened!")
    endMenu.eMenu()