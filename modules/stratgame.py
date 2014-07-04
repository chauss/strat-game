'''
Created on 29.03.2014

@author: Chris
'''
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

def main():
    gameData = GameData()
    defaultGameDataTwoPlayer(gameData)
    
    #p1name = raw_input("Please enter the name of the first player: ")
    #p2name = raw_input("Please enter the name of the second player: ")
    
    gameData.playerOne = Player("Chris", 1)
    gameData.playerTwo = Player("Laura", 2)
    
    pf = playingfield.PlayingField(gameData)
    tokenSet = buildDefaultTokenSet(gameData)
    tp = TokenPlacing(pf, tokenSet, gameData)
    m = Movement(pf, gameData, OneFieldPerMove())
    
    # Start the Console reader in a new Thread
    cr = ConsoleReader(gameData, pf, tp, m)
    cr.start()
    
    app = wx.App(False)
    frame = MainWindow(None, gameData)
    app.MainLoop()
    
    tui = TextualUserInterface.Tui(pf, gameData)
    pf.attach(tui)

    cr.join()
    
    
if __name__ == '__main__':
    main()