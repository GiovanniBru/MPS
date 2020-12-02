# -*- coding: utf-8 -*-

from business.model.funcionario import *

class GerenteDeRH(Funcionario):
  def __init__(self, nome, cpf, cargo, salario, login, senha):
    super().__init__(nome, cpf, cargo, salario, login, senha)

  