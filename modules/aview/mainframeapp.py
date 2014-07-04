'''
Created on 22.04.2014

@author: Chris
'''
import wx
from menuBar import MenuBar

class MainWindow(wx.Frame):
    def __init__(self, parent, gameData):
        
        wx.Frame.__init__(self, parent, title="StratGame", size=(800, 600),
                          style=wx.RESIZE_BORDER | wx.DEFAULT_FRAME_STYLE)
        self.gameData = gameData
        self.CreateStatusBar()
        
        self.SetMenuBar(MenuBar(self, self.gameData))
        
        self.Show(True)
        
        
        
