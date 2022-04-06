'''
Created on 05-04-2022

@author: dsanmartins
'''

from model.Client import Client

class ClientController():
    
    def __init__(self):
        pass
        
    def createClient(self,dni,name):
        client = Client(dni,name)
        return client
        
