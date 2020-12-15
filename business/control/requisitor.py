from business.model.database import *
from business.model.notificacaoSalario import *

    #self.database=Database()
    #database.appendNotificacao(notificacao)
  def requisicao():
    database=Database()
    if(vontade==1):
      print("Digite seu novo salário: ", end="")
      salario = input()
      print("Digite uma mensagem,explicando o motivo da mudanca: ", end="")
      mensagem = input()
      usuario=database.logado
      gerenterh="flavio" #Aqui poderia ser feita uma logica para achar o gerente resposável pelo setor
      reqMudarSalario(usuario,mensagem,salario,gerenterh)
    elif(vontade==2):
      cargo="gerente"
      print("Digite sua nova data para comeco das ferias: ", end="")
      data = input()
      print("Digite uma mensagem,explicando o motivo da mudanca: ", end="")
      mensagem = input()
      while((validaData(data)==-31)):
          print("Digite sua data no formato DD/MM/AAAA: ", end="")
          data = input()
      data=validaData(d_nascimento)
      usuario=database.logado
      gerenterh="flavio"
      reqMudarFerias(usuario,mensagem,data,gerenterh)
  
  def reqMudarSalario(login,mensagem,valor,gerenterh):
    database=Database()
    notificacao = NotificacaoSalario(login,gerenterh,mensagem,valor)
    database.appendNotificacao(notificacao)

  def aceitarMudarSalario():
    pass
  
  def rejeitarMudarSalario():
    pass

  def reqMudarFerias(login,mensagem,data,gerenterh):
    database=Database()
    notificacao = NotificacaoFerias(self,remetente,destinatario,mensagem,data)
    database.appendNotificacao(notificacao)

  def aceitarMudarFerias():
    pass
  
  def rejeitarMudarFerias():
    pass


    