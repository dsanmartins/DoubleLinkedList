'''
Created on 04-04-2022

@author: dsanmartins
'''
import names
import random

class Generator:
    
    def __init__(self):
        pass
    
    def generateName(self):
        return names.get_full_name() 
    
    def generateDni(self):
        idStr = repr(random.randrange(9, 10**9))
        newId= idStr[:8] + "-" + idStr[:1]
        return newId