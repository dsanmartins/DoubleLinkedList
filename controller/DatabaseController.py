'''
Created on 04-04-2022

@author: dsanmartins
'''
from model.utils.Database import Database
from controller.NodeListController import NodeListController

class DatabaseController():
    
    def __init__(self):
        pass
    
    def populateDatabase(self):
        database = Database()
        database.create()
        
    def getClient(self,filename):
        nodeListController = NodeListController()
        nodeList = nodeListController.getNodeList()
        database = Database()
        list_ = database.getData(filename)
        for i in range(len(list_)):
            nodeList.addNode(list_[i])
        return nodeList
    