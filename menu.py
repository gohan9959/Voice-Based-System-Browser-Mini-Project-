import sqlFunctions as sfun
import voiceParse as vp
import dbRequest as dbr
import urlQuery
import forBrowser
def options():
   op= str()
   print("1.Open Files or Folders\n2.Open URL\n3.Update Database\n4.Change Default Browser To Open URLs\n5.Exit\nSelect an Option:")
   op=vp.query("1")
   if(op == '1' or "files" in op.lower() or "folders" in op.lower() or "file" in op.lower() or "folder" in op.lower()):
      print("What Should I Open?")
      qry=vp.query("1")
      sfun.getValues(qry)
   elif(op == '2' or "url" in op.lower()):
      print("What URL Should I Open?")
      qry=vp.query("1")
      urlQuery.open(qry)
   elif(op == '3' or "update" in op.lower() or "database" in op.lower()):
      dbr.request()
   elif(op == '4' or 'browser' in op.lower() or 'default' in op.lower()):
      forBrowser.setDefaultBrowser()
   elif(op == '5' or "exit" in op.lower()):
      print("Bye!!")
   else:
      print("Invalid Choice")
      options()