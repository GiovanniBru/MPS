class NotificacaoSalario(Notificacao):
  def __init__(self,remetente,destinatario,mensagem,valor):
    super().__init__(remetente,destinatario,mensagem)
    self.valor=valor
  
  def notifica():
    pass
    