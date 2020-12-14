# -*- coding: utf-8 -*-

from business.model.funcionario import *

class Gerente(Funcionario):
  def __init__(self, nome, cpf, cargo, login, senha,data_nascimento,salario=4000):
	  super().__init__(nome, cpf, cargo, login, senha,salario, data_nascimento)