'''
Created on 04-04-2022

@author: dsanmartins
'''
from controller.DatabaseController import DatabaseController
from controller.ClientController import ClientController
from controller.NodeListController import NodeListController

databaseController = DatabaseController()
clientController = ClientController()
nodeListController = NodeListController()

databaseController.populateDatabase()
clientList = databaseController.getClient("clients.csv")

print("***** Please chose an option ******")
print("[1] Print the list")
print("[2] Add a new client")
print("[3] Search for a client")
print("[4] Delete a client")
choice = input("?")
while True:
    
    if choice =='1':
        lst = clientList.printList()
        for i in lst:
            print(i.getDni(),i.getName())
    elif choice =='2':
        clientDni = input("DNI of the client?")
        clientName = input("Name of the client?")
        clientList.addNode(clientController.createClient(clientDni,clientName))
    elif choice =='3':
        try:
            clientDni = input("Search by DNI")
            client = clientList.searchByDni(clientDni)
            print("The client exist in the database!")
            print("")
        except(Exception,AttributeError):
            print("Client does not exist")
    elif choice == '4':
        clientDni = input("DNI of the client?")
        result = clientList.deleteNode(clientDni)
        if result:
            print("The client was deleted!")
        else:
            print("We do not find the client!")
    elif int(choice) > 4: #Or whatever end condition
        print("Bye!")
        break
    
    
    print("***** Please chose an option? ******")
    print("[1] Print the list")
    print("[2] Add a new client")
    print("[3] Search for a client")
    print("[4] Delete a client")
    choice = input("?")
    



