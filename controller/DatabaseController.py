'''
Created on 04-04-2022

@author: dsanmartins
'''

from model.utils.Database import Database

class DatabaseController():
    
    def __init__(self):
        pass
    
    def populateDatabase(self):
        database = Database()
        database.create()
        
    def getClient(self,filename):
        database = Database()
        return database.getData(filename)
        
    