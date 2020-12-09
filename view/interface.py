# -*- coding: utf-8 -*-

def mostraMenu():
	print("============= PAPERFLY =============")
	print("1 - Cadastrar Usuário")
	print("2 - Logar como Usuário")
	print("3 - Listar Usuário por tipo")
	print("4 - Editar Usuário")
	print("5 - Remover Usuário")
	print("6 - Sair")
	print("\nEscolha: ", end="")

def mostraMenuDeCadastro():
	print("\n=========== CADASTRAR ===========")
	print("Qual tipo de usuário você deseja cadastrar? ")
	print("1 - Vendedor")
	print("2 - Gerente")
	print("3 - Gerente de RH")
	print("\nEscolha: ", end="")

def mostraMenuDeListagem():
  print("============ LISTAR USUÁRIOS ============")
  print("\n1 - Listar Vendedor")
  print("2 - Listar Gerente")
  print("3 - Listar Gerente de RH")
  print("4 - Todos")
  print("5 - Voltar")
  print("\nEscolha: ", end="")

def mostraTipoListagemVendedor():
  print("============ LISTAR VENDEDOR ============")
  print("1 - Listar por Ordem Alfabética")
  print("2 - Listar pelo maior salário")
  print("3 - Voltar")
  print("\nEscolha: ", end="")

def mostraMenuDeEdicao():
  print("============ EDITAR USUÁRIO ============")
  print("Digite o nome do usuário a ser editado: ", end="")

def mostraMenuDeRemocao():
  print("============ REMOVER USUÁRIO ============")
  print("Digite o login do usuário a ser removido: ", end="")
  


