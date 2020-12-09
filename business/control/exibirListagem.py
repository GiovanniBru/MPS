from business.model.database import *

def exibir(vontade):
  if(vontade==1):
    usrfilter="vendedor"
  elif(vontade==2):
    usrfilter="gerente"
  elif(vontade==3):
    usrfilter="gerentederh"
  elif(vontade==4):
    usrfilter=""
  database=Database()
  listing=database.showDatabase()
  for x in listing:
    string=""
    for keys,value in x.items():
      string+=str(value)+(' ' * (13-len(str(value))))+"|"
      
    if(usrfilter+" " in string):
      #print("{:20s}".format(str(value)),end="")
      print(string,end="")
    print("")
  
  #print ('\n'.join(table))
  input("\n Pressioner enter para sair...")
  