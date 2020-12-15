class NotificacaoFerias(Notificacao):
  def __init__(self,remetente,destinatario,mensagem,data):
    super().__init__(remetente,destinatario,mensagem)
    self.data=data
  
  def notifica():
    pass