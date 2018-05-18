import folderOpen as fo
import speech_recognition as sr    
r = sr.Recognizer()  
with sr.Microphone() as source:
    print("What Should I Open?")  
    audio = r.listen(source)  
try:  
   request=r.recognize_google(audio)
   print(request)
except sr.UnknownValueError:  
   print("Could not understand audio")  
except sr.RequestError as e:  
   print("Could not Request Results{0}".format(e))
fo.op(request)
