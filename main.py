# -*- coding: utf-8 -*-

from business.model.vendedor import *
from view.interface import *
from view.login_password import *
from business.control.cadastro import cadastrar
from business.control.exibirListagem import exibir
from business.control.removerUsuario import removerUsuario


import os

#CarlosVendedor = Vendedor("Carlos", "213.432.654-12", "Vendedor", 1064.23)


while(True):
  mostraMenu()
  vontade = int(input())

  if(vontade == 1):
    os.system('clear')
    mostraMenuDeCadastro()
    vontade = int(input())
    cadastrar(vontade)
    os.system('clear')
  elif(vontade == 2):
    os.system('clear')
    mostraLoginESenha()
  elif(vontade == 3):
    mostraMenuDeListagem()
    vontade=int(input())
    if(vontade == 5):
      os.system('clear')
      continue
    os.system('clear')
    exibir(vontade)
    os.system('clear')
  elif(vontade == 4):
    mostraMenuDeEdicao()
  elif(vontade == 5):
    mostraMenuDeRemocao()
    if(removerUsuario()):
      print("Usuário removido com sucesso")
    else:
      print("Usuário não encontrado")
    input("Digite qualquer caracter para voltar ao menu:")

    os.system('clear')
  elif(vontade == 6):
    print("Obrigado por utilizar nossa aplicação")
    exit()
  else:
    print("Fora do escopo, fechando programa")
    exit()
# CarlosVendedor.getDados()
