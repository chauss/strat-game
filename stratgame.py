'''
Created on 29.03.2014

@author: Chris
'''
import sys, os
appPath = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(1, os.path.join(appPath, "modules"))
sys.path.insert(1, os.path.join(appPath, "modules", "aview"))
sys.path.insert(1, os.path.join(appPath, "modules", "aview", "dialogs"))
sys.path.insert(1, os.path.join(appPath, "modules", "controller"))
sys.path.insert(1, os.path.join(appPath, "modules", "model"))
sys.path.insert(1, os.path.join(appPath, "modules", "util"))
sys.path.insert(1, os.path.join(appPath, "config"))

import wx
import TextualUserInterface as TextualUserInterface
from mainframeapp import MainWindow
import playingfield as playingfield
from player import Player
from gameDataTwoPlayer import GameData
from gameDataFiller import defaultGameDataTwoPlayer
from tokenSetBuilder import buildDefaultTokenSet
from tokenPlacing import TokenPlacing
from movement import Movement
from consoleReader import ConsoleReader
from movementRules import OneFieldPerMove
import logging.config

def main():
    logging.config.fileConfig(os.path.join(appPath + '\\config\\log.config'))
    
    gameData = GameData()
    defaultGameDataTwoPlayer(gameData)
    
    gameData.playerOne = Player("Chris", 1)
    gameData.playerTwo = Player("Laura", 2)
    
    pf = playingfield.PlayingField(gameData)
    tokenSet = buildDefaultTokenSet(gameData)
    tp = TokenPlacing(pf, tokenSet, gameData)
    m = Movement(pf, gameData, OneFieldPerMove())
    
    tui = TextualUserInterface.Tui(pf, gameData)
    tui.update()
    pf.attach(tui)
    
    # Start the Console reader in a new Thread
    cr = ConsoleReader(gameData, pf, tp, m)
    cr.start()
    
    app = wx.App(False)
    MainWindow(None, gameData)
    app.MainLoop()

    cr.shutdown()
    
    
if __name__ == '__main__':
    main()