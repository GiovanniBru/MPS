from business.model.database import *

def realizarPagamentosFolha():
  database=Database()
  for typeusr in database.database:
    for usr in typeusr:
      pagar(usr)


def gerarRecibo():
  pass

def pagar(usr):
  CPF=usr.getCPF()
  nome=usr.getNome()
  salario=usr.getSalario()
  Banco=1 #usr.getBanco()
  agencia =1#usr.getAgenciaBancaria()
  conta =1#usr.getContaBancaria()
  #Aqui iriam adaptações importantes e códigos de segurança para permitir o uso da API IUGU
  transferirIUGU(CPF,nome,salario,Banco,agencia,conta)


def transferirIUGU(CPF,nome,salario,Banco,agencia,conta): #Utiliza a plataforma de pagamentos IUGU isolando códigos anteriores de peculiaridades da adaptação para a API e possibilitando a troca de plataforma de pagamento
  pass