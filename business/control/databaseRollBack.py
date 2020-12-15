from business.model.database import *

class DatabaseRollBack():
  def __init__(self):
    self.dados=0
  
  def saveChanges(self):
    self.dados=Database().database

  def rollBackChange(self):
    if(self.dados!=0):
      Database().setDatabase(self.dados)
      return 1
    else:
      return 0
