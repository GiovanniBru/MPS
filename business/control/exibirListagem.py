from business.model.database import *

def exibir():
  database=Database()
  database.showDatabase()
  if(input()):
    print("saindo...")
  