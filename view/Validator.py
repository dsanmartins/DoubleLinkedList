'''
Created on 14-04-2022

@author: https://codingshiksha.com/
'''
import wx

class NotEmptyValidator(wx.PyValidator):
    
    def __init__(self):
        wx.PyValidator.__init__(self)
 
    def Clone(self):
        """
        Note that every validator must implement the Clone() method.
        """
        return NotEmptyValidator()
 
    def Validate(self, win):
        textCtrl = self.GetWindow()
        text = textCtrl.GetValue()
        if len(text) == 0:
            wx.MessageBox("This field must contain some text!", "Error")
            textCtrl.SetBackgroundColour("pink")
            textCtrl.SetFocus()
            textCtrl.Refresh()
            return False
        else:
            textCtrl.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
            textCtrl.Refresh()
            return True
 
    def TransferToWindow(self):
        return True
 
    def TransferFromWindow(self):
        return True
