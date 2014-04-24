'''
Created on 24.04.2014

@author: Chris
'''
import wx

class MenuBar(wx.MenuBar):
    def __init__(self, parent):
        super(MenuBar, self).__init__()
        self.parent = parent
        self._createControls()
        
    def _createControls(self):
        
        
        filemenu = wx.Menu()
        filemenu.Append(wx.ID_ABOUT, "&About", "Information about this program")
        filemenu.AppendSeparator()
        filemenu.Append(wx.ID_EXIT, "E&xit", "Terminates the program")
        
        self.Append(filemenu, "&File")
        
        wx.EVT_MENU(self, wx.ID_EXIT, self.onExit)
        
    def onExit(self, event):
        self.parent.Close()