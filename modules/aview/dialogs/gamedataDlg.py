'''
Created on 24.04.2014

@author: Chris
'''
import wx


class GameDataDlg(wx.Dialog):
    def __init__(self, parent, gameData):
        super(GameDataDlg, self).__init__(parent=parent, size=wx.Size(300, 170),
                                       style=wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER)
        self.SetTitle("Gamedata")
        
        self.gameData = gameData
        
        self.createControls()
        
        
        
    def createControls(self):
        mainSizer = wx.FlexGridSizer(2, 4, 0, 0)
        
        