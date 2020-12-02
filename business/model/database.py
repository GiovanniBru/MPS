
class DatabaseMeta(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class Database(metaclass=DatabaseMeta):
  def __init__(self):
    self.database=[[],[],[]]
  def appendVendedor(self,x):
    self.database[0].append(x)

  def appendGerente(self,x):
    self.database[1].append(x)

  def appendGerenteRH(self,x):
    self.database[2].append(x)
  
  def showDatabase(self):
    for i in self.database:
      for j in i:
        print(j)



