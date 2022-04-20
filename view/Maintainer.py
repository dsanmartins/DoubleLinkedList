import wx
import wx.grid as gridlib
import wx.lib.masked as masked
from wx.grid import GridCellAutoWrapStringRenderer

from controller.DatabaseController import DatabaseController
from controller.ClientController import ClientController
from controller.NodeListController import NodeListController


class Maintainer(wx.Frame):
    def __init__(self):
        
        # Controladores los cuales son usados por la Vista
        self.databaseController = DatabaseController()
        self.clientController = ClientController()
        self.nodeListController = NodeListController()
        self.databaseController.populateDatabase()
        self.clientList = self.databaseController.getClient("clients.csv")
        
        # Ventana principal: Tiene  un nombre, un estilo por defecto 
        # (no se puede maximizar y cambiar el tamanho
        # Tiene un tamnho de 800x600
        wx.Frame.__init__(self, None, title="Mantenedor de Clientes", style = wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX),size=(800,600))
        
        # Un panel donde seran compuestos los widgets
        self.panel = wx.Panel(self)
        
        # Una barra de estado en el fondo de la ventana principal
        self.CreateStatusBar()
        # Se crea un menu pequenho
        filemenu= wx.Menu()
        # Se crea un separador
        filemenu.AppendSeparator()
        # Entrada de menu para salir de la aplicacion
        menuExit = filemenu.Append(wx.ID_EXIT,"E&xit"," Terminate the program")
        # Entrada de menu para mostrar informacion sobre la aplicacion
        menuAbout = filemenu.Append(wx.ID_ABOUT, "&About"," Information about this program")
        # Se enlazan las entradas del menu con acciones representadas por metodos
        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)
        self.Show(True)
        # Se crea una barra de menu donde ira el menu crado
        menuBar = wx.MenuBar()
        # Se adicionan los menus
        menuBar.Append(filemenu,"&File") # Adding the "filemenu" to the MenuBar
        # Se adiciona la barra del menu en la ventana principal
        self.SetMenuBar(menuBar)  # Adding the MenuBar to the Frame content.
        
        # Se crean los controles (widgets) en el panel de la ventana principal
        # StaticBox: un panel con nombre para agrupar controles 
        # StaticText: Labels o etiquetas
        # TextCtrl: Entradas de texto para ingresa la informacion
        # masked: enmascarar la entrada de texto
        self.box1 = wx.StaticBox(self.panel, wx.ID_ANY, "Ingresar Cliente", pos=(10,0),size=(790, 100))
        self.lbl1 = wx.StaticText(self.box1, -1, 'DNI:', pos =(10,25))
        self.txt1 = masked.TextCtrl(self.box1, style=wx.TE_LEFT, size=(120, 25), name = "txt1", pos = (50,23),  mask = '##.###.###-#')
        self.lbl2 = wx.StaticText(self.box1, -1, 'Nombre:', pos =(180,25))
        self.txt2 = wx.TextCtrl(self.box1, style=wx.TE_LEFT, size=(250, 25), name = "txt2", pos = (245,23))
        self.btn1 = wx.Button(self.box1, label = "Guardar", size=(100, 25), pos=(505,23)) 
        
        self.box2 = wx.StaticBox(self.panel, wx.ID_ANY, "Buscar Cliente", pos=(5,105),size=(790, 100))
        self.lbl2 = wx.StaticText(self.box2, -1, 'DNI:', pos =(10,25))
        self.txt3 = masked.TextCtrl(self.box2, style=wx.TE_LEFT, size=(120, 25), name = "txt3", pos = (50,23),  mask = '##.###.###-#')
        self.btn2 = wx.Button(self.box2, label = "Buscar", size=(100, 25), pos=(180,23)) 
        
        self.box3 = wx.StaticBox(self.panel, wx.ID_ANY, "Eliminar Cliente", pos=(5,205),size=(790, 100))
        self.lbl3 = wx.StaticText(self.box3, -1, 'DNI:', pos =(10,25))
        self.txt4 = masked.TextCtrl(self.box3, style=wx.TE_LEFT, size=(120, 25), name = "txt4", pos = (50,23),  mask = '##.###.###-#')
        self.btn3 = wx.Button(self.box3, label = "Eliminar", size=(100, 25), pos=(180,23)) 
        
        # Se crea una grilla sobre el panel para mostrar los datos
        self.grid = gridlib.Grid(self.panel,-1,pos=(5,320))
        self.grid.SetDefaultRenderer(GridCellAutoWrapStringRenderer())
        # La grilla tendrá un total de filas igual al total de datos de la lista y dos columnas
        total = len(self.clientList.printList())
        self.grid.CreateGrid(total, 2)
        # Se crean los nombres de las columnas
        self.grid.SetColLabelValue(0, "DNI")
        self.grid.SetColLabelValue(1, "Nombre")
        # Si la lista es vacia, entonces crear una fila vacia
        if len(self.clientList.printList()) ==0:
            self.grid.SetCellValue(0,0,"Empty")
            self.grid.SetCellValue(0,1,"Empty")
        else:
            # Si la lista no esta vacia llenarla usando el metodo loadData()
            self.loadData()
        
        # Ancho de las columnas
        self.grid.SetColSize(0, 120)        
        self.grid.SetColSize(1, 470)

        # Adicionar los controles en un BoxSizer (layout) para organizar de forma vertical
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.box1, 0, wx.TOP|wx.BOTTOM|wx.ALIGN_CENTER_HORIZONTAL, 5)
        self.sizer.Add(self.box2, 0, wx.TOP|wx.BOTTOM|wx.ALIGN_CENTER_HORIZONTAL, 5)
        self.sizer.Add(self.box3, 0, wx.TOP|wx.BOTTOM|wx.ALIGN_CENTER_HORIZONTAL, 5)
        self.sizer.Add(self.grid, 4, wx.EXPAND )
        self.panel.SetSizer(self.sizer) 
     
     
        # Eventos de Botones (Guardar, Buscar y Eliminar)
        self.btn1.Bind(wx.EVT_BUTTON, self.OnSaveClient)
        self.btn2.Bind(wx.EVT_BUTTON, self.OnSearchClient)
        self.btn3.Bind(wx.EVT_BUTTON, self.OnDeleteClient)
   
    # Metodo para guardar cliente
    def OnSaveClient(self,e):
        # Verificar si el nombre no esta vacio. 
        # Se debe verificar que el DNI tampoco este vacio (Implementar)
        if self.txt2.GetLineLength(0) == 0: 
            # Crear un dialogo  
            dls= wx.MessageDialog( self, "El nombre no puede estar vacio", "Dialogo", wx.OK)
            # Mostrarlo
            dls.ShowModal()
            # Eliminarlo 
            dls.Destroy() 
        else:
            # Si el tamanho del nombre es mayor  a cero, guardarlo
            self.clientList.addNode(self.clientController.createClient(self.txt1.GetLineText(0).replace('.',''),self.txt2.GetLineText(0)))
            # Limpiar la grilla
            self.grid.ClearGrid()
            # Eliminar todas las filas
            self.grid.DeleteRows(pos=0, numRows=self.grid.GetNumberRows(), updateLabels=True)
            # Insertar la cantidad de filas de acuerdo al numero de datos de la lista
            self.grid.InsertRows(pos=0, numRows=len(self.clientList.printList()), updateLabels=True)
            # Llenar la grilla con los datos actualizados
            self.loadData()
            dls= wx.MessageDialog( self, 'Cliente Guardado!', "Dialogo", wx.OK)
            dls.ShowModal() 
            dls.Destroy()
        # Limpiar las entradas de texto 
        self.txt1.Clear()
        self.txt2.Clear()
    
    # Buscar un cliente
    def OnSearchClient(self,e):
        # Se asume que la grilla esta en sincronia con la lista
        # Por lo tanto solo se hace una busqueda en la grilla, recorriendo la columna DNI
        op = 1
        for row in range(0,self.grid.GetNumberRows()):
            item = self.grid.GetCellValue(row, 0)
            # Si el DNI del cliente es igual al DNI buscado
            if item == self.txt3.GetLineText(0).replace('.',''):
                dls= wx.MessageDialog( self, 'El cliente se encuentra en la fila '+ str(row+1) , "Dialogo", wx.OK)
                dls.ShowModal()
                dls.Destroy()
                op = 0
                break
        if op == 1:
            dls= wx.MessageDialog( self, 'El cliente No encontrado!' , "Dialogo", wx.OK)
            dls.ShowModal()
            dls.Destroy()
        self.txt3.Clear()
    
    # Eliminar un cliente    
    def OnDeleteClient(self,e):
        # Si se ha encontrado y borrado el cliente de la lista retorna Verdadero
        # en caso contrario retorna Falso
        result = self.clientList.deleteNode(self.txt4.GetLineText(0).replace('.','')) 
        if result:
            # Las mismas operaciones para limpiar y cargar datos en la grilla descritas en adicionar cliente 
            self.grid.ClearGrid()
            self.grid.DeleteRows(pos=0, numRows=self.grid.GetNumberRows(), updateLabels=True)
            self.grid.InsertRows(pos=0, numRows=len(self.clientList.printList()), updateLabels=True)
            self.loadData()
            dls= wx.MessageDialog( self, 'Cliente Eliminado!', "Dialogo", wx.OK)
            dls.ShowModal() 
            dls.Destroy() 
        else:
            dls= wx.MessageDialog( self, 'Cliente No encontrado!', "Dialogo", wx.OK)
            dls.ShowModal() # Show it
            dls.Destroy() # finally destroy it when finished 
        
        self.txt4.Clear()
    
    # Metodo que especifica el comportamiento del about del menu    
    def OnAbout(self,e):
        # A message dialog box with an OK button. wx.OK is a standard ID in wxWidgets.
        dlg = wx.MessageDialog( self, "Un mantenedor de clientes", "Sobre el mantenedor", wx.OK)
        dlg.ShowModal() # Show it
        dlg.Destroy() # finally destroy it when finished.

    # Metodo para salir del aplicativo
    def OnExit(self,e):
        self.Close(True)  # Close the frame.

    # Metodo para cargar la grilla con los datos de la lista de clientes.
    def loadData(self):
        for index, value in enumerate(self.clientList.printList()):
            self.grid.SetCellValue(index, 0, value.getDni())
            self.grid.SetCellValue(index, 1, value.getName())
        