'''
Created on 04-04-2022

@author: dsanmartins
'''

from model.utils.Generator import Generator
from model.Client import Client
import csv

class Database:
    
    def __init__(self):
        pass
    
    def create(self):
        
        client = []
        for i in range(1,50):
            dataClient = Generator()
            data = i,dataClient.generateDni(),dataClient.generateName()
            client.append(data)
           
        with open('clients.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(client)   
    
    def getData(self,filename):
        client = []
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                client.append(Client(row[1], row[2]))    
        
        return client
        
        
        
        