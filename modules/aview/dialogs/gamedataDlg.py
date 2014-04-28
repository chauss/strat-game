'''
Created on 24.04.2014

@author: Chris
'''
import wx
import wx.lib.intctrl
import copy


class GameDataDlg(wx.Dialog):
    def __init__(self, parent, gameData):
        super(GameDataDlg, self).__init__(parent=parent, size=wx.Size(300, 170),
                                       style=wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER)
        self.SetTitle("Gamedata")
        self._dataHasChanged = False
        
        self.gameData = gameData
        self.changedGameData = copy.copy(self.gameData)
        
        self.createControls()
        self.createEvents()
        
        
        
    def createControls(self):
        dataSizer = wx.FlexGridSizer(2, 2, 0, 0)
        
        dataSizer.Add(self.buildGeneralBox(), 0, wx.ALL|wx.CENTER, 5)
        dataSizer.Add(self.buildPlayerBox(), 0, wx.ALL|wx.CENTER, 5)
        dataSizer.Add(self.buildPlayingFieldBox(), 0, wx.ALL|wx.CENTER, 5)
        
        buttonSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.btnOk = wx.Button(self, wx.ID_OK, label='Ok')
        self.btnCancel = wx.Button(self, wx.ID_CANCEL, label='Cancel')
        
        buttonSizer.Add(self.btnOk, 0, wx.ALL|wx.CENTER, 5)
        buttonSizer.Add(self.btnCancel, 0, wx.ALL|wx.CENTER, 5)
        
        
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        mainSizer.Add(dataSizer, 0, wx.ALL|wx.CENTER, 5)
        mainSizer.Add(buttonSizer, 0, wx.ALL|wx.CENTER, 5)
        
        self.SetSizer(mainSizer)
        self.Fit()
        
        
    def buildGeneralBox(self):
        generalBox = wx.StaticBox(self, wx.ID_ANY, label='General')
        generalSizer = wx.StaticBoxSizer(generalBox, wx.VERTICAL)
        flxGridSz = wx.FlexGridSizer(3, 2, 0, 0)
        
        lblTokensPerPlayer = wx.StaticText(self, label='Tokens per player: ')
        self.intTokensPerPlayer = wx.lib.intctrl.IntCtrl(self, style=wx.TE_CENTER,
                                              value=self.gameData.tokensPerPlayer)
        
        lblPlayerCount = wx.StaticText(self, label='Playercount: ')
        self.intPlayerCount = wx.lib.intctrl.IntCtrl(self, style=wx.TE_CENTER,
                                                     value=self.gameData.playerCount)
        self.intPlayerCount.Enable(False)
        
        lblGameState = wx.StaticText(self, label='GameState: ')
        self.txtGameState = wx.TextCtrl(self, style=wx.TE_CENTER)
        self.txtGameState.Enable(False)
        
        flxGridSz.Add(lblTokensPerPlayer, 0, wx.ALL, 5)
        flxGridSz.Add(self.intTokensPerPlayer, 0, wx.ALL, 5)
        flxGridSz.Add(lblPlayerCount, 0, wx.ALL, 5)
        flxGridSz.Add(self.intPlayerCount, 0, wx.ALL, 5)
        flxGridSz.Add(lblGameState, 0, wx.ALL, 5)
        flxGridSz.Add(self.txtGameState, 0, wx.ALL, 5)
        
        generalSizer.Add(flxGridSz, 0, wx.ALL|wx.CENTER, 5)
        
        return generalSizer
    
    def buildPlayerBox(self):
        playerBox = wx.StaticBox(self, wx.ID_ANY, label='Players')
        playerSizer = wx.StaticBoxSizer(playerBox, wx.VERTICAL)
        flxGridSz = wx.FlexGridSizer(3, 2, 0, 0)
        
        lblPlayerOne = wx.StaticText(self, label='Player one: ')
        self.txtPlayerOne = wx.TextCtrl(self, style=wx.TE_CENTER,
                                        value=self.gameData.playerOne.getName())
        
        lblPlayerTwo = wx.StaticText(self, label='Player two: ')
        self.txtPlayerTwo = wx.TextCtrl(self, style=wx.TE_CENTER,
                                        value=self.gameData.playerTwo.getName())
        
        flxGridSz.Add(lblPlayerOne, 0, wx.ALL, 5)
        flxGridSz.Add(self.txtPlayerOne, 0, wx.ALL, 5)
        flxGridSz.Add(lblPlayerTwo, 0, wx.ALL, 5)
        flxGridSz.Add(self.txtPlayerTwo, 0, wx.ALL, 5)
        
        playerSizer.Add(flxGridSz, 0, wx.ALL|wx.CENTER, 5)
        
        return playerSizer
        
    def buildPlayingFieldBox(self):
        playingFieldBox = wx.StaticBox(self, wx.ID_ANY, label='Playingfield')
        playingFieldSizer = wx.StaticBoxSizer(playingFieldBox, wx.VERTICAL)
        flxGridSz = wx.FlexGridSizer(3, 2, 0, 0)
        flxGridSz.AddGrowableCol(1)
        
        lblHeight = wx.StaticText(self, label='Height: ')
        self.intHeight = wx.lib.intctrl.IntCtrl(self, style=wx.TE_CENTER,
                                                value=self.gameData.fieldHeight)
        
        lblWidth = wx.StaticText(self, label='Width: ')
        self.intWidth = wx.lib.intctrl.IntCtrl(self, style=wx.TE_CENTER,
                                               value=self.gameData.fieldWidth)
        
        lblAreaLaneLimit = wx.StaticText(self, label='Area lane limit: ')
        self.intAreaLaneLimit = wx.lib.intctrl.IntCtrl(self, style=wx.TE_CENTER,
                                                       value=self.gameData.areaLanesLimit)
        
        flxGridSz.Add(lblHeight, 0, wx.ALL, 5)
        flxGridSz.Add(self.intHeight, 0, wx.ALL, 5)
        flxGridSz.Add(lblWidth, 0, wx.ALL, 5)
        flxGridSz.Add(self.intWidth, 0, wx.ALL, 5)
        flxGridSz.Add(lblAreaLaneLimit, 0, wx.ALL, 5)
        flxGridSz.Add(self.intAreaLaneLimit, 0, wx.ALL, 5)
        
        playingFieldSizer.Add(flxGridSz, 0, wx.ALL|wx.CENTER, 5)
        
        return playingFieldSizer
        
    def createEvents(self):
        # general
        wx.EVT_TEXT(self, self.intTokensPerPlayer.GetId(), self.onTokensPerPlayer)
        wx.EVT_TEXT(self, self.intPlayerCount.GetId(), self.onPlayerCount)
        # players
        wx.EVT_TEXT(self, self.txtPlayerOne.GetId(), self.onDataChanged)
        wx.EVT_TEXT(self, self.txtPlayerTwo.GetId(), self.onDataChanged)
        # playingfield
        wx.EVT_TEXT(self, self.intHeight.GetId(), self.onHeight)
        wx.EVT_TEXT(self, self.intWidth.GetId(), self.onWidth)
        wx.EVT_TEXT(self, self.intAreaLaneLimit.GetId(), self.onAreaLaneLimit)
        # buttons
        wx.EVT_BUTTON(self, self.btnOk.GetId(), self.onOk)
        wx.EVT_BUTTON(self, self.btnCancel.GetId(), self.onCancel)
        
    def onTokensPerPlayer(self, event):
        try:
            self.changedGameData.tokensPerPlayer = self.intTokensPerPlayer.GetValue()
        except ValueError as e:
            self.intTokensPerPlayer.SetValue(1)
            wx.MessageBox(str(e), 'Info', 
                          wx.OK | wx.ICON_INFORMATION)
        self.onDataChanged()
        
    def onPlayerCount(self, event):
        try:
            self.changedGameData.playerCount = self.intPlayerCount.GetValue()
        except ValueError as e:
            self.intPlayerCount.SetValue(2)
            wx.MessageBox(str(e), 'Info', 
                          wx.OK | wx.ICON_INFORMATION)
        self.onDataChanged()
        
    def onHeight(self, event):
        try:
            self.changedGameData.fieldHeight = self.intHeight.GetValue()
        except ValueError as e:
            self.intHeight.SetValue(2)
            wx.MessageBox(str(e), 'Info', 
                          wx.OK | wx.ICON_INFORMATION)
        self.onDataChanged()
        
    def onWidth(self, event):
        try:
            self.changedGameData.fieldWidth = self.intWidth.GetValue()
        except ValueError as e:
            self.intWidth.SetValue(1)
            wx.MessageBox(str(e), 'Info', 
                          wx.OK | wx.ICON_INFORMATION)
        self.onDataChanged()
        
    def onAreaLaneLimit(self, event):
        try:
            self.changedGameData.areaLaneLimit = self.intAreaLaneLimit.GetValue()
        except ValueError as e:
            self.intAreaLaneLimit.SetValue(1)
            wx.MessageBox(str(e), 'Info', 
                          wx.OK | wx.ICON_INFORMATION)
        self.onDataChanged()
        
    def onDataChanged(self, event=None):
        self._dataHasChanged = True
        
    def onOk(self, event):
        if self._dataHasChanged:
            self.gameData = self.changedGameData
            self.EndModal(wx.ID_OK)
        else:
            self.EndModal(wx.ID_CANCEL)
            
    def onCancel(self, event):
        if self._dataHasChanged and \
            wx.MessageBox('Changes has been made! Chancel anyway?', 'Info',
                          wx.YES_NO | wx.ICON_INFORMATION) == wx.NO:
            return
        self.EndModal(wx.ID_CANCEL)
        
        