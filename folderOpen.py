import os
import sys
def op(request):
    path=""
    y="f"
    x=y+":"
    for root, dirs, files in os.walk(x,topdown=True):
        for name in dirs:
            path=os.path.join(root, name)
            print(path)
            s1=path.split("\\")
            s2=path.split(":")
            if(request.lower()==s1[len(s1)-1].lower() or request.lower()==s2[len(s2)-1].lower()):
                os.startfile(path)
                sys.exit(0)
