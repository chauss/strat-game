'''
Created on 29.03.2014

@author: Chris
'''
import aview.TextualUserInterface as TextualUserInterface
import modules.controller.playingfield as playingfield
import model.token.Token as Token
import model.player.Player as Player

def main():
    p1name = raw_input("Please enter the name of the first player: ")
    p2name = raw_input("Please enter the name of the second player: ")
    
    p1 = Player(p1name, 1)
    p2 = Player(p2name, 2)
    
    pf = playingfield.PlayingField(10, 5, 15)
    pf.build()
    p1Top = pf.buildTopStartArea()
    p2Bot = pf.buildBottomStartArea()
    
    tui = TextualUserInterface.Tui(pf)
    pf.attach(tui)
    p = Player("Chris", 1)
    t = Token(3, p)
    pf.placeToken(t, 3, 3)
    
    
if __name__ == '__main__':
    main()