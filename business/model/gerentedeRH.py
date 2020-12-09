# -*- coding: utf-8 -*-

from business.model.funcionario import *

class GerenteDeRH(Funcionario):
  def __init__(self, nome, cpf, cargo, login, senha,salario=4000):
	  super().__init__(nome, cpf, cargo, login, senha,salario)

  