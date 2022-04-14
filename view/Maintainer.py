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
        # Setting up the menu.
        filemenu= wx.Menu()
        filemenu.AppendSeparator()
        menuExit = filemenu.Append(wx.ID_EXIT,"E&xit"," Terminate the program")
        menuAbout = filemenu.Append(wx.ID_ABOUT, "&About"," Information about this program")
        # Set events.
        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)
        self.Show(True)
        # Creating the menubar.
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu,"&File") # Adding the "filemenu" to the MenuBar
        self.SetMenuBar(menuBar)  # Adding the MenuBar to the Frame content.
        
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
        
    
        self.grid = gridlib.Grid(self.panel,-1,pos=(5,320))
        self.grid.SetDefaultRenderer(GridCellAutoWrapStringRenderer())
        total = len(self.clientList.printList())
        self.grid.CreateGrid(total, 2)
        self.grid.SetColLabelValue(0, "DNI")
        self.grid.SetColLabelValue(1, "Nombre")
        if len(self.clientList.printList()) ==0:
            self.grid.SetCellValue(0,0,"Empty")
            self.grid.SetCellValue(0,1,"Empty")
        else:
            for index, value in enumerate(self.clientList.printList()):
                self.grid.SetCellValue(index, 0, value.getDni())
                self.grid.SetCellValue(index, 1, value.getName())
        
        self.grid.SetColSize(0, 120)        
        self.grid.SetColSize(1, 470)

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.box1, 0, wx.TOP|wx.BOTTOM|wx.ALIGN_CENTER_HORIZONTAL, 5)
        self.sizer.Add(self.box2, 0, wx.TOP|wx.BOTTOM|wx.ALIGN_CENTER_HORIZONTAL, 5)
        self.sizer.Add(self.box3, 0, wx.TOP|wx.BOTTOM|wx.ALIGN_CENTER_HORIZONTAL, 5)
        self.sizer.Add(self.grid, 4, wx.EXPAND )
        self.panel.SetSizer(self.sizer) 
    
   
    def OnAbout(self,e):
        # A message dialog box with an OK button. wx.OK is a standard ID in wxWidgets.
        dlg = wx.MessageDialog( self, "Un mantenedor de clientes", "Sobre el mantenedor", wx.OK)
        dlg.ShowModal() # Show it
        dlg.Destroy() # finally destroy it when finished.

    def OnExit(self,e):
        self.Close(True)  # Close the frame.

