'''
Created on 04-04-2022

@author: dsanmartins
'''
class Client:
    
    def __init__(self,dni,name):
        self.__dni= dni
        self.__name=name
        
    def setName(self,name):
        self.__name=name
        
    def setDni(self,dni):
        self.__dni=dni
        
    def getName(self):
        return self.__name
    
    def getDni(self):
        return self.__dni