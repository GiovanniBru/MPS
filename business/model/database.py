class DatabaseMeta(type):
  _instances = {}

  def __call__(cls, *args, **kwargs):
    if (cls not in cls._instances):
      instance = super().__call__(*args, **kwargs)
      cls._instances[cls] = instance
    return cls._instances[cls]

class Database(metaclass=DatabaseMeta):
  def __init__(self):
    self.database=[[],[],[]]
  def appendVendedor(x):
    self.database[0].append(x)

  def appendGerente(x):
    self.database[1].append(x)

  def appendGerenteRH(x):
    self.database[2].append(x)
    


