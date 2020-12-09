# -*- coding: utf-8 -*-

from business.model.vendedor import *
from business.model.funcionario import *
from business.model.gerentedeRH import *
from business.model.gerente import *
from business.model.database import *
from business.control.validaCadastro import *
from infra.HandleDatabase import *

def cadastrar(vontade):
  if(vontade==1):
    cargo="vendedor"
  elif(vontade==2):
    cargo="gerente"
  elif(vontade==3):
    cargo="gerentederh"
  database = Database()
  print("Digite seu nome: ", end="")
  nome = input()
  if (not validaNome(nome)==1):
    print("####Cadastro cancelado####")
    input("Pressioner enter para sair")
    return -1
  print("Digite seu CPF: ", end="")
  CPF = input()
  print("Digite um login para sua conta: ", end="")
  login = input()
  validaLogin(login)
  print("Digite uma senha para sua conta: ", end="")
  senha = input()
  validaSenha(senha)
  print("Cadastro realizado com sucesso!")
  if(cargo=="gerente"):
    gerente = Gerente(nome, CPF, "gerente", login, senha)
    database.appendGerente(gerente)
  elif(cargo=="gerentederh"):
    gerentederh = GerenteDeRH(nome,CPF, "gerentederh", login, senha)
    database.appendGerenteRH(gerentederh)
  elif(cargo=="vendedor"):
    vendedor = Vendedor(nome, CPF, "vendedor", login, senha)
    print(vendedor)
    database.appendVendedor(vendedor)
  saveDatabase(database.database)
