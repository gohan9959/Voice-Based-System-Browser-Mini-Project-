import folderOpen as fo
import voiceParse as vp
def options():
   op=""
   print("1.Start\n2.Exit\nSelect Option:")
   op=vp.query("1")
   if(op == '1' or op.lower() == 'start'):
      print("What Should I Open?")
      qry=vp.query("1")
      fo.op(qry)
   elif(op == '2' or op.lower() == 'exit'):
      print("Bye!!")
   else:
      print("Invalid Choice")
      options()  
