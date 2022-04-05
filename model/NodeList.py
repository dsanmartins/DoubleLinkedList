'''
Created on 04-04-2022

@author: dsanmartins
'''
from model.Node import Node

class NodeList:
    
    def __init__(self):
        self.__head = Node(None,None,None)
        self.__tail = Node(None,None,None)
    
    def addNode(self,client):
        newNode = Node(None,None,client)
        if self.isEmpty():
            self.__head.setNext_(newNode)
            newNode.setPrevious(self.__head)
            self.__tail = newNode
        else:
            self.__tail.setNext_(newNode)
            newNode.setPrevious(self.__tail)
            self.__tail = newNode
        
    def isEmpty(self):
        if self.__head.getNext_() is None:
            return True
        else:
            return False 
      
    def printList(self):
        if not self.isEmpty():
            node = self.__head.getNext_()
            while (node is not None):
                print("DNI", node.getClient().getDni(),"Name",node.getClient().getName())
                node = node.getNext_()
            
    def searchByDni(self,dni):
        if not self.isEmpty():
            node = self.__head.getNext_()
            while (node is not None):
                if node.getClient().getDni() == dni:
                    return node.getClient()
                node = node.getNext_()
    