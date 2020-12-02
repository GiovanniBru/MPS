# -*- coding: utf-8 -*-

from business.model.vendedor import *
from business.model.funcionario import *
from business.model.gerentedeRH import *
from business.model.gerente import *
from business.model.database import *
from business.control.validaCadastro import *

def cadastrar():
  
  database = Database()
  database.appendVendedor(Vendedor("teste", 12345, "vendedor", "teste", "teste123"))
  print("Digite seu nome: ", end="")
  nome = input()
  if (not validaNome(nome)):
    print("Cadastro cancelado", end="")
    return -1

  print("Digite seu cargo: ", end="")
  cargo = input()
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
  elif(cargo=="gerenterh"):
    gerentederh = GerenteDeRH(nome, "gerentederh", CPF, login, senha)
    database.appendGerenteRH(gerentederh)
  elif(cargo=="vendedor"):
    vendedor = Vendedor(nome, CPF, "vendedor", login, senha)
    print(vendedor)
    database.appendVendedor(vendedor)
