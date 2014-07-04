'''
Created on 24.04.2014

@author: Chris
'''
import wx
import subprocess
from aboutDlg import AboutDlg
from gamedataDlg import GameDataDlg

ID_SHOW_GAMEDATA = wx.NewId()
ID_OPEN_CONSOLE = wx.NewId()

class MenuBar(wx.MenuBar):
    def __init__(self, parent, gameData):
        super(MenuBar, self).__init__()
        self.gameData = gameData
        self.parent = parent
        self._createControls()
        
    def _createControls(self):
        # FILE
        filemenu = wx.Menu()
        filemenu.Append(ID_SHOW_GAMEDATA, "Show &GameData", "Shows the current GameData")
        filemenu.AppendSeparator()
        filemenu.Append(wx.ID_EXIT, "&Exit", "Terminates the program")
        
        self.Append(filemenu, "&File")
        
        # EXTRAS
        filemenu = wx.Menu()
        filemenu.Append(ID_OPEN_CONSOLE, "&Open Console", "Opens the console / tui")
        
        self.Append(filemenu, "&Extras")
        # HELP
        filemenu = wx.Menu()
        filemenu.Append(wx.ID_ABOUT, "&About", "Information about this program")
        
        self.Append(filemenu, "&Help")
        
        # EVENT MANAGEMENT
        wx.EVT_MENU(self, wx.ID_EXIT, self.onExit)
        wx.EVT_MENU(self, ID_SHOW_GAMEDATA, self.onShowGamedata)
        wx.EVT_MENU(self, ID_OPEN_CONSOLE, self.openConsole)
        wx.EVT_MENU(self, wx.ID_ABOUT, self.onAbout)
        
    def onExit(self, event):
        self.parent.Close()
        
    def onShowGamedata(self, event):
        dlg = GameDataDlg(self, self.gameData)
        if dlg.ShowModal() == wx.ID_OK:
            self.gameData = dlg.gameData
        dlg.Destroy()
        
    def openConsole(self, event):
        #subprocess.call()
        # TODO: need to call the tui
        pass
        
    def onAbout(self, event):
        dlg = AboutDlg(self)
        dlg.ShowModal()
        dlg.Destroy()
    
    
        
