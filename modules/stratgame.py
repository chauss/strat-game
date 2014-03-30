'''
Created on 29.03.2014

@author: Chris
'''
import aview.TextualUserInterface as TextualUserInterface
import model.playingfield as playingfield
import model.token as token
import model.player as player

def main():
    pf = playingfield.PlayingField(10, 10)
    pf.build()
    tui = TextualUserInterface.Tui(pf)
    pf.attach(tui)
    p = player.Player("Chris", 1)
    t = token.Token(3, p)
    pf.placeToken(t, 3, 3)
    
    
if __name__ == '__main__':
    main()