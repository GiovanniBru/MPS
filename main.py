# -*- coding: utf-8 -*-

from business.model.vendedor import *
from view.interface import *
from business.control.cadastro import cadastrar
import os

#CarlosVendedor = Vendedor("Carlos", "213.432.654-12", "Vendedor", 1064.23)


while(True):
  mostraMenu()
  vontade = int(input())

  if(vontade == 1):
    mostraMenuDeCadastro()
    vontade = int(input())
    if(vontade == 1):
      cadastrar()
    os.system('clear')
  elif(vontade == 2):
    os.system('clear')
    pass
  elif(vontade == 3):
    mostraMenuDeListagem()
    os.system('clear')
  elif(vontade == 4):
    mostraMenuDeEdicao()
    os.system('clear')
  elif(vontade == 5):
    mostraMenuDeRemocao()
    os.system('clear')
  elif(vontade == 6):
    print("Obrigado por utilizar nossa aplicação")
    exit()
  else:
    print("Fora do escopo, fechando programa")
    exit()
# CarlosVendedor.getDados()