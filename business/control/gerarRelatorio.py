class geraRelatorioLogin():
  def __init__(self):
    self.dados=buscarDados()
  
  def gerar(self):
    formatarDados()
    organizarDados()
    salvarArquivo()

  def buscarDados(self):
    #return Database().logs
    pass
  
  def formatarDados(self):
    #for x in self.dados:
    #   
    pass
  
  def organizarDados(self):
    pass
  
  def salvarArquivo(self):
    saveFileAsTxt()
    pass

  def saveFileAsTxt(self):
    pass

class geraRelatorioLoginPdf(geraRelatorioLogin):
  def __init__(self):
    super().__init__()

  def organizarDados(self):
    pass

  def salvarArquivo(self):
    saveFileAsPdf()
    pass
  
  def saveFileAsPdf(self):
    pass

class geraRelatorioLoginHtml(geraRelatorioLogin):
  def __init__(self):
    super().__init__()

  def organizarDados(self):
    pass

  def salvarArquivo(self):
    saveFileAsPdf()
    pass
  
  def saveFileAsHtml(self):
    pass
