from business.model.database import *

def exibir():
  database=Database()
  listing=database.showDatabase()
  for x in listing:
    for keys,value in x.items():
      print(str(value)+"\t", end="")
    print("")
  if(input()):
    print("saindo...")
  