'''
Created on 29.03.2014

@author: Chris
'''
import aview.TextualUserInterface as TextualUserInterface
import modules.controller.playingfield as playingfield
import model.token.Token as Token
import model.player.Player as Player
import model.gameDataTwoPlayer.GameData as GameData
import controller.gameDataFiller.defaultGameDataTwoPlayer as defaultGameDataTwoPlayer

def main():
    gameData = GameData()
    defaultGameDataTwoPlayer(gameData)
    
    p1name = raw_input("Please enter the name of the first player: ")
    p2name = raw_input("Please enter the name of the second player: ")
    
    gameData.setPlayerOne(Player(p1name, 1))
    gameData.setPlayerTwo(Player(p2name, 2))
    
    pf = playingfield.PlayingField(gameData)

    
    tui = TextualUserInterface.Tui(pf)
    pf.attach(tui)
    

    
    
if __name__ == '__main__':
    main()