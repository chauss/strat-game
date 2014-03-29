'''
Created on 29.03.2014

@author: Chris
'''
import aview.TextualUserInterface as TextualUserInterface
import model.playingfield as playingfield

def main():
    pf = playingfield.PlayingField(10, 10)
    TextualUserInterface.Tui(pf)
    
    
if __name__ == '__main__':
    main()