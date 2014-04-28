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
from threading import Thread
from movementRules import OneFieldPerMove

def main():
    gameData = GameData()
    defaultGameDataTwoPlayer(gameData)
    
    #p1name = raw_input("Please enter the name of the first player: ")
    #p2name = raw_input("Please enter the name of the second player: ")
    
    gameData.playerOne = Player("Chris", 1)
    gameData.playerTwo = Player("Laura", 2)
    
    pf = playingfield.PlayingField(gameData)
    
    frame = MainWindow(None, gameData)
    gui_thread = Thread(target= frame.run(frame))
    
    
    
    tui = TextualUserInterface.Tui(pf, gameData)
    pf.attach(tui)

    tokenSet = buildDefaultTokenSet(gameData)
    tp = TokenPlacing(pf, tokenSet, gameData)

    m = Movement(pf, gameData, OneFieldPerMove())
    
    cr = ConsoleReader(gameData, pf, tp, m)
    cr_thread = Thread(target= cr.run())
    cr_thread.start()
    cr_thread.join()
    gui_thread.start()
    gui_thread.join()
    
    
if __name__ == '__main__':
    main()