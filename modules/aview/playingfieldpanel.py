'''
Created on 29.04.2014

@author: Chris
'''
import wx


class PlayingFieldPanel(wx.Panel):
    def __init__(self, parent, gameData, playingField):
        wx.Panel.__init__(parent)
        
        self.gameData = gameData
        self.playingField = playingField
        