'''
Created on 04-04-2022

@author: dsanmartins
'''
class Node:
  
    def __init__(self,previous,next_,client):
        self.__previous=previous
        self.__next_=next_
        self.__client=client

    def getPrevious(self):
        return self.__previous

    def getNext_(self):
        return self.__next_

    def setPrevious(self, value):
        self.__previous = value

    def setNext_(self, value):
        self.__next_ = value

    def getClient(self):
        return self.__client
    
    def setClient(self,client):
        self.__client=client