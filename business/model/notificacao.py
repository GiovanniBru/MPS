from datetime import datetime

class Notificacao():
  def __init__(self,remetente,destinatario,mensagem):
    self.remetente=remetente
    self.destinatario=destinatario
    self.mensagem=mensagem
    self.data_envio=datetime.now()
  
  def notifica():
    pass