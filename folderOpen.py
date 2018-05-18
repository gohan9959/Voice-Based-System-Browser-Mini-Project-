import os
import sys
def op(request):
    path=""
    y="f"
    x=y+":"
    if(request.lower()!="exit"):
        for root, dirs, files in os.walk(x,topdown=True):
           for name in dirs:
                a=os.path.join(root, name)
                print(a)
                s=a.split(":" or "\\")
                if(request.lower()==s[len(s)-1].lower()):
                    path=a
                    os.startfile(path)
                    sys.exit(0)
            
    else:
        sys.exit(0)

