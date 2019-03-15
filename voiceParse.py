import speech_recognition as sr
import time
import menu
def query():
    r = sr.Recognizer()  
    with sr.Microphone() as source:
        audio = r.listen(source)  
    try:  
        request=r.recognize_google(audio)
        print(request)
        flg=1
    except sr.UnknownValueError:  
        print("Could not understand audio")
        flg=0  
    except sr.RequestError as e:  
        print("Could not Request Results{0}".format(e))
        flg=-1
    if(flg==1):
        time.sleep(3)
        return request
    elif(flg==0):
        menu.options()
    elif(flg==-1):
        print("Exited!!")
