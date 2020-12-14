# -*- coding: utf-8 -*-

from business.model.funcionario import *

class Vendedor(Funcionario):
	def __init__(self, nome, cpf, cargo, login, senha, data_nascimento,salario=2000):
		super().__init__(nome, cpf, cargo, login, senha,salario, data_nascimento)

	def getDados(self):
		print("Nome: " + self.getNome() + 
			"\nCPF: " + self.getCPF() + 
			"\nCargo: "	+ self.getCargo() + 
			"\nSalario: " + str(self.getSalario()) +
      "\nLogin: " + self.getLogin() + 
      "\nSenha: " + self.getSenha() +
      "\nData de Nascimento: " + self.getDataNascimento)
