'''
Created on 08.07.2014

@author: Chris
'''
import TextualUserInterface as TextualUserInterface
import playingfield as playingfield
from player import Player
from gameDataTwoPlayer import GameData
from gameDataFiller import defaultGameDataTwoPlayer
from tokenSetBuilder import buildDefaultTokenSet
from tokenPlacing import TokenPlacing
from movement import Movement
from movementRules import OneFieldPerMove


class TwoManGame():
    
    def __init__(self):
        # get new GameData-object and fill with default
        self.__gd = GameData()
        defaultGameDataTwoPlayer(self.__gd)
        self.__gd.playerOne = Player("PlayerOne", 1)
        self.__gd.playerTwo = Player("PlayerTwo", 2)
        
        # Create PlayingField and TokenSet
        self.__pf = playingfield.PlayingField(self.__gd)
        tokenSet = buildDefaultTokenSet(self.__gd)
        
        # Get TokenPlacing- and Movement-object
        self.__tp = TokenPlacing(self.__pf, tokenSet, self.__gd)
        self.__m = Movement(self.__pf, self.__gd, OneFieldPerMove())
        
        self.__tui = TextualUserInterface.Tui(self.__pf, self.__gd)
        self.__tui.update()
        self.__pf.attach(self.__tui)
        
    def getGameDatas(self):
        '''Returns a tuple with all hold gameDatas:
        GameData(),
        PlayingField(),
        TokenPlacing(),
        Movement()
        '''
        return (self.__gd, self.__pf, self.__tp, self.__m)