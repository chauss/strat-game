'''
Created on 24.04.2014

@author: Chris
'''
import wx
from aboutDlg import AboutDlg

ID_SHOW_GAMEDATA = wx.NewId()

class MenuBar(wx.MenuBar):
    def __init__(self, parent):
        super(MenuBar, self).__init__()
        self.parent = parent
        self._createControls()
        
    def _createControls(self):
        # FILE
        filemenu = wx.Menu()
        filemenu.Append(ID_SHOW_GAMEDATA, "Show &GameData", "Shows the current GameData")
        filemenu.AppendSeparator()
        filemenu.Append(wx.ID_EXIT, "&Exit", "Terminates the program")
        
        self.Append(filemenu, "&File")
        
        # HELP
        filemenu = wx.Menu()
        filemenu.Append(wx.ID_ABOUT, "&About", "Information about this program")
        
        self.Append(filemenu, "&Help")
        
        # EVENT MANAGEMENT
        wx.EVT_MENU(self, wx.ID_EXIT, self.onExit)
        wx.EVT_MENU(self, ID_SHOW_GAMEDATA, self.onShowGamedata)
        wx.EVT_MENU(self, wx.ID_ABOUT, self.onAbout)
        
    def onExit(self, event):
        self.parent.Close()
        
    def onShowGamedata(self, event):
        pass
    
    def onAbout(self, event):
        dlg = AboutDlg(self)
        dlg.ShowModal()
    
    
        
