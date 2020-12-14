# -*- coding: utf-8 -*-

from business.model.funcionario import *

class GerenteDeRH(Funcionario):
  def __init__(self, nome, cpf, cargo, login, senha,data_nascimento,salario=4000):
	  super().__init__(nome, cpf, cargo, login, senha,salario, data_nascimento)

  def mudarSalario(user,value):
    database=Database()
    nrole,reference=database.getReferenceTo(key)
    if(not reference==0):
      reference.setSalario(value)
      return 1
    return 0

  def mudarFerias(user,value):
    database=Database()
    nrole,reference=database.getReferenceTo(key)
    if(not reference==0):
      reference.setSalario(value)
      return 1
    return 0

  def mudarFerias(user,value):
    database=Database()
    nrole,reference=database.getReferenceTo(key)
    if(not reference==0):
      reference.setFerias(value)
      return 1
    return 0
  