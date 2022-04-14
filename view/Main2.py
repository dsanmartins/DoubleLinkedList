'''
Created on 13-04-2022

@author: dsanmartins
'''
import wx
from view.Maintainer import Maintainer
        
if __name__ == "__main__":
    app = wx.App()
    Maintainer().Show()
    app.MainLoop()