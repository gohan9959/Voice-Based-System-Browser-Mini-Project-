import speech_recognition as sr
import time
import menu
import endMenu
import openFileOrDir as ofd
def query(wm):
    r = sr.Recognizer()  
    with sr.Microphone() as source:
        audio = r.listen(source)  
    try:  
        request=r.recognize_google(audio)
        print(request.capitalize())
        flg=1
    except sr.UnknownValueError:  
        print("Could not understand audio")
        flg=0  
    except sr.RequestError as e:  
        print("Could not Request Results{0}".format(e))
        flg=-1
    if(flg==1):
        return request
    elif(flg==0):
        if(wm == "1"):
            menu.options()
        elif(wm == "2"):
            endMenu.eMenu()
        elif(wm == "3"):
            ofd.open()
        else:
            print("Unknown Path!!")
    elif(flg==-1):
        print("Exited!!")
