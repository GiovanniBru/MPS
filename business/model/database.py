
def dump(obj):
  userData={}
  for attr in dir(obj):
    #attr = _Funcionario.__login
    if(attr.startswith("_") and not attr.endswith("__")):
      userData[attr]=getattr(obj, attr)
  return userData


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
    listing=[]
    for i in self.database:
      for j in i:
        listing.append(dump(j))
    return listing

  def __getReferenceTo(self,key):
    userData={}
    toexclude=0
    for cargo in database:
      for entry in cargo:
        for attr in dir(entry):
          #attr = _Funcionario.__login
          if(attr.Contains("__login") and getattr(entry, attr)==key ):
            return cargo,entry

  def removeUser(self,key):
    exclude=self.__getReferenceTo(key)
    database.remove(exclude)
    
    



