'''
Created on 31.03.2014

@author: Chris
'''
from myExceptions import DataNotSetError
from player import Player
from area import Area
import logging.config

logging.config.fileConfig('C:\\Users\\Chris\\git\\stratgame\\config\\log.config')
logger = logging.getLogger('model')

TOKEN_PLACING = 0
TOKEN_MOVING = 1
GAME_FINISHED = 2

class GameData(object):
    '''
    this class is some kind of container for all the data
    that is needed for one game
    '''
    def __init__(self):
        self.__playerCount = 2
        self.__fieldHeight = 0
        self.__fieldWidth = 0
        self.__tokensPerPlayer = 0
        self.__playerOne = None
        self.__playerTwo = None
        self.__topArea = None
        self.__bottomArea = None
        self.__AreaLanesLimit = 0
        self.__activePlayer = None
        self.__gameState = TOKEN_PLACING
        self.__winner = None
        
    '''Setters for the gameData >>>>>>>>>>>'''
    def setFieldHeight(self, height):
        '''
        sets the height of a field: must be at least 2
        '''
        if height < 2:
            logger.debug("Tried to set height=%d but must be at least 2" % height)
            raise ValueError("FieldHeight must be at least 2")
        self.__fieldHeight = height
        
    def setFieldWidth(self, width):
        '''
        sets the width of the field: must be at least 1
        '''
        if width < 1:
            logger.debug("Tried to set width=%d but must be at least 1" % width)
            raise ValueError("FieldWidth must be at least 1")
        self.__fieldWidth = width
        
    def setTokensPerPlayer(self, tokens):
        '''
        sets the tokens per player: must be at least 1
        '''
        if tokens < 1:
            logger.debug("Tried to set TokensPerPlayer=%d but must be at least 1" % tokens)
            raise ValueError("TokensPerPlayer must be at least 1")
        self.__tokensPerPlayer = tokens
        
    def setPlayerOne(self, player):
        '''
        sets the first player: must differ from second player
        '''
        if self.__playerTwo:
            if player.getIndex() == self.__playerTwo.getIndex():
                logger.debug("Tried to set PlayerOne with the same index as PlayerTwo")
                raise ValueError("PlayerOne must have a index that differs from PlayerTwo's index")
        self.__playerOne = player
        
    def setPlayerTwo(self, player):
        '''
        sets the second player: must differ from first player
        '''
        if self.__playerOne:
            if player.getIndex() == self.__playerOne.getIndex():
                logger.debug("Tried to set PlayerTwo with the same index as PlayerOne")
                raise ValueError("PlayerTwo must have a index that differs from PlayerOne's index")
        self.__playerTwo = player
        
    def setTopArea(self, area):
        '''
        sets the top area: must be instance of Area
        '''
        if not isinstance(area, Area):
            logger.debug("Tried to set topArea which is not instance of Area")
            raise ValueError("area must be instance of Area")
        self.__topArea = area
    
    def setBottomArea(self, area):
        '''
        sets the bottom area: must be instance of Area
        '''
        if not isinstance(area, Area):
            logger.debug("Tried to set topArea which is not instance of Area")
            raise ValueError("area must be instance of Area")
        self.__bottomArea = area
        
    def setAreaLanesLimit(self, limit):
        '''
        Can only be called if fieldWidth and tokensPerPlayer
        have already been set or raises an ValueError
        '''
        if (limit * self.fieldWidth()) < self.tokensPerPlayer():
            logger.debug("Tried to set too small limit=%d" % limit)
            raise ValueError("The limit is to small for the game conditions")
        self.__AreaLanesLimit = limit
        
    def setActivePlayer(self, player):
        '''
        this sets the player whos turn it is right now
        '''
        self.__activePlayer = player
        
    def nextGameState(self):
        '''
        this increases the gamestate to the next state
        '''
        self.__gameState += 1
        
    def setWinner(self, player):
        '''
        sets the winner on one of the playing players
        '''
        if player == self.__playerOne or player == self.__playerTwo:
            self.__winner = player
        else:
            raise ValueError("The winning player is not part of the playing players")
        
###############################################################################
    '''Getters for the gameData >>>>>>>>>>>'''
###############################################################################


    def playerCount(self):
        '''
        returns the playerCount
        '''
        return self.__playerCount
        
    def fieldHeight(self):
        '''
        returns the fieldHeight
        '''
        if self.__fieldHeight != 0:
            return self.__fieldHeight
        else:
            raise DataNotSetError("fieldHeight")
    
    def fieldWidth(self):
        '''
        returns the fieldWidth
        '''
        if self.__fieldWidth != 0:
            return self.__fieldWidth
        else:
            raise DataNotSetError("fieldWidth")
    
    def tokensPerPlayer(self):
        '''
        returns the tokensPerPlayer
        '''
        if self.__tokensPerPlayer != 0:
            return self.__tokensPerPlayer
        else:
            raise DataNotSetError("tokensPerPlayer")
    
    def playerOne(self):
        '''
        returns the playerOne
        '''
        if self.__playerOne:
            return self.__playerOne
        else:
            raise DataNotSetError("playerOne")
    
    def playerTwo(self):
        '''
        returns the playerTwo
        '''
        if self.__playerTwo:
            return self.__playerTwo
        else:
            raise DataNotSetError("playerTwo")
        
    def topArea(self):
        '''
        returns the topArea
        '''
        if self.__topArea:
            return self.__topArea
        else:
            raise DataNotSetError("topArea")
        
    def bottomArea(self):
        '''
        returns the bottomArea
        '''
        if self.__bottomArea:
            return self.__bottomArea
        else:
            raise DataNotSetError("bottomArea")
        
    def AreaLanesLimit(self):
        '''
        returns the fieldHeight
        '''
        return self.__AreaLanesLimit
    
    def activePlayer(self):
        '''
        returns the player whos turn it is
        '''
        return self.__activePlayer
    
    def gameState(self):
        '''
        returns the current gameState
        '''
        return self.__gameState
    
    def winner(self):
        '''
        returns the winner of the game
        '''
        return self.__winner
