'''
Created on 29.03.2014

@author: Chris
'''
import aview.TextualUserInterface as TextualUserInterface
import modules.controller.playingfield as playingfield
from model.player import Player
from model.gameDataTwoPlayer import GameData
from controller.gameDataFiller import defaultGameDataTwoPlayer
from controller.tokenSetBuilder import buildDefaultTokenSet
from controller.tokenPlacing import TokenPlacing
from controller.movement import Movement
from controller.consoleReader import ConsoleReader
from threading import Thread

def main():
    gameData = GameData()
    defaultGameDataTwoPlayer(gameData)
    
    #p1name = raw_input("Please enter the name of the first player: ")
    #p2name = raw_input("Please enter the name of the second player: ")
    
    gameData.setPlayerOne(Player("Chris", 1))
    gameData.setPlayerTwo(Player("Laura", 2))
    
    pf = playingfield.PlayingField(gameData)
    
    tui = TextualUserInterface.Tui(pf, gameData)
    pf.attach(tui)

    tokenSet = buildDefaultTokenSet(gameData)
    tp = TokenPlacing(pf, tokenSet, gameData)

    m = Movement(pf, gameData)
    
    cr = ConsoleReader(gameData, pf, tp, m)
    cr_thread = Thread(target= cr.run())
    cr_thread.start()
    cr_thread.join()
    
    
if __name__ == '__main__':
    main()