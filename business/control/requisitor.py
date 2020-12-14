from business.model.database import *


class RequisitorMeta(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class Requisitor(metaclass=DatabaseMeta):
  def __init__(self):
    #Classe que Singleton Factory para geração de requisições de mudança de férias e salário