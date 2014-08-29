'''
Created on 24.04.2014

@author: Chris
'''
import wx
import version as v

class AboutDlg(wx.Dialog):
    def __init__(self, parent):
        super(AboutDlg, self).__init__(parent=parent, size=wx.Size(300, 170))
        self.SetTitle("About")
        
        self.createControls()
        
        
    def createControls(self):
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        myFont = wx.Font(14, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_SLANT, wx.FONTWEIGHT_NORMAL)
        
        author = "Author: " + str(v.author())
        lblAuthor = wx.StaticText(self, label=author)
        lblAuthor.SetFont(myFont)
        
        version = "Version: " + str(v.version())
        lblVersion = wx.StaticText(self, label=version)
        lblVersion.SetFont(myFont)
        
        version_type = "Version-Type: " + str(v.version_type())
        lblType = wx.StaticText(self, label=version_type)
        lblType.SetFont(myFont)
        
        btnOk = wx.Button(self, wx.ID_OK, label="Ok")
        
        mainSizer.Add(wx.StaticText(self))
        mainSizer.Add(lblAuthor, flag=wx.ALIGN_CENTER)
        mainSizer.Add(lblVersion, flag=wx.ALIGN_CENTER)
        mainSizer.Add(lblType, flag=wx.ALIGN_CENTER)
        mainSizer.Add(wx.StaticText(self))
        mainSizer.Add(btnOk, flag=wx.ALIGN_CENTER)
        
        wx.EVT_BUTTON(self, wx.ID_OK, self.onOk)
        
        self.SetSizer(mainSizer, wx.CENTER_FRAME)
        
        
    def onOk(self, event):
        self.EndModal(wx.ID_OK)