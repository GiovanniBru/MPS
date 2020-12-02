from business.model.database import *

def removeUsr(key):
  database=Database()
  nrole,exclude=database.getReferenceTo(key)
  if(not exclude==0):
    database.database[nrole].remove(exclude)
    return 1
  return 0

def removerUsuario():
  login=input()
  return removeUsr(login)
