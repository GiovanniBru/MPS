import pickle

def saveDatabase(database):
  with open('database.data', 'wb') as filehandle:
    # store the data as binary data stream
    pickle.dump(database, filehandle)
  
def loadDatabase():
  with open('database.data', 'rb') as filehandle:
    # read the data as binary data stream
    return pickle.load(filehandle)