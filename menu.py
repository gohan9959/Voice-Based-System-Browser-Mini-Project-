import sqlFunctions as sfun
import voiceParse as vp
import dbRequest as dbr
def options():
   op=""
   print("1.Start\n2.Update Database\n3.Exit\nSelect an Option:")
   op=vp.query("1")
   if(op == '1' or op.lower() == 'start'):
      print("What Should I Open?")
      qry=vp.query("1")
      sfun.getValues(qry)
   elif(op == '2' or op.lower() == "update database" or op.lower == "update" or op.lower == "database"):
      dbr.request()
   elif(op == '3' or op.lower() == 'exit'):
      print("Bye!!")
   else:
      print("Invalid Choice")
      options()