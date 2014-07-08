'''
Created on 31.03.2014

@author: Chris
'''
from myExceptions import DataNotSetError
from area import Area
import logging

logger = logging.getLogger('model.gdtp')

PRE_GAME = 0
TOKEN_PLACING = 1
TOKEN_MOVING = 2
GAME_FINISHED = 3

class GameData(object):
    '''
    this class is some kind of container for all the data
    that is needed for one game
    '''
    def __init__(self):
        self.__fieldHeight = 0
        self.__fieldWidth = 0
        self.__tokensPerPlayer = 0
        self.__playerOne = None
        self.__playerTwo = None
        self.__topArea = None
        self.__bottomArea = None
        self.__areaLanesLimit = 0
        self.__activePlayer = None
        self.__playerCount = 2
        self.__gameState = PRE_GAME
        self.__winner = None
        
    @property
    def fieldHeight(self):
        '''
        returns the fieldHeight
        '''
        if self.__fieldHeight != 0:
            return self.__fieldHeight
        else:
            raise DataNotSetError("fieldHeight")
        
    @fieldHeight.setter
    def fieldHeight(self, fieldHeight):
        '''
        sets the height of a field: must be at least 2
        '''
        if fieldHeight < 2:
            logger.debug("Tried to set height=%d but must be at least 2" % fieldHeight)
            raise ValueError("FieldHeight must be at least 2")
        self.__fieldHeight = fieldHeight
        
        
    @property
    def fieldWidth(self):
        '''
        returns the fieldWidth
        '''
        if self.__fieldWidth != 0:
            return self.__fieldWidth
        else:
            raise DataNotSetError("fieldWidth")
        
    @fieldWidth.setter
    def fieldWidth(self, width):
        '''
        sets the width of the field: must be at least 1
        '''
        if width < 1:
            logger.debug("Tried to set width=%d but must be at least 1" % width)
            raise ValueError("FieldWidth must be at least 1")
        self.__fieldWidth = width
        
    
    @property
    def tokensPerPlayer(self):
        '''
        returns the tokensPerPlayer
        '''
        if self.__tokensPerPlayer != 0:
            return self.__tokensPerPlayer
        else:
            raise DataNotSetError("tokensPerPlayer")
    
    @tokensPerPlayer.setter
    def tokensPerPlayer(self, tokens):
        '''
        sets the tokens per player: must be at least 1
        '''
        if tokens < 1:
            logger.debug("Tried to set TokensPerPlayer=%d but must be at least 1" % tokens)
            raise ValueError("TokensPerPlayer must be at least 1")
        maxTokens = (self.__fieldHeight / 2) * self.__fieldWidth
        if tokens > maxTokens:
            logger.debug("Tried to set TokensPerPlayer=%d but can max be %d" % (tokens, maxTokens))
            raise ValueError("To much TokensPerPlayer for current playingfield")
        self.__tokensPerPlayer = tokens
        
        
    @property
    def playerOne(self):
        '''
        returns the playerOne
        '''
        if self.__playerOne:
            return self.__playerOne
        else:
            raise DataNotSetError("playerOne")
        
    @playerOne.setter
    def playerOne(self, player):
        '''
        sets the first player: must differ from second player
        '''
        if self.__playerTwo:
            if player.getIndex() == self.__playerTwo.getIndex():
                logger.debug("Tried to set PlayerOne with the same index as PlayerTwo")
                raise ValueError("PlayerOne must have a index that differs from PlayerTwo's index")
        self.__playerOne = player
        
        
    @property
    def playerTwo(self):
        '''
        returns the playerTwo
        '''
        if self.__playerTwo:
            return self.__playerTwo
        else:
            raise DataNotSetError("playerTwo")
        
    @playerTwo.setter
    def playerTwo(self, player):
        '''
        sets the second player: must differ from first player
        '''
        if self.__playerOne:
            if player.getIndex() == self.__playerOne.getIndex():
                logger.debug("Tried to set PlayerTwo with the same index as PlayerOne")
                raise ValueError("PlayerTwo must have a index that differs from PlayerOne's index")
        self.__playerTwo = player
        
        
    @property
    def topArea(self):
        '''
        returns the topArea
        '''
        if self.__topArea:
            return self.__topArea
        else:
            raise DataNotSetError("topArea")
        
    @topArea.setter
    def topArea(self, area):
        '''
        sets the top area: must be instance of Area
        '''
        if not isinstance(area, Area):
            logger.debug("Tried to set topArea which is not instance of Area")
            raise ValueError("area must be instance of Area")
        self.__topArea = area
    
    
    @property
    def bottomArea(self):
        '''
        returns the bottomArea
        '''
        if self.__bottomArea:
            return self.__bottomArea
        else:
            raise DataNotSetError("bottomArea")
        
    @bottomArea.setter
    def bottomArea(self, area):
        '''
        sets the bottom area: must be instance of Area
        '''
        if not isinstance(area, Area):
            logger.debug("Tried to set topArea which is not instance of Area")
            raise ValueError("area must be instance of Area")
        self.__bottomArea = area
        
        
    @property
    def areaLanesLimit(self):
        '''
        returns the fieldHeight
        '''
        return self.__areaLanesLimit
    
    @areaLanesLimit.setter
    def areaLanesLimit(self, limit):
        '''
        Can only be called if fieldWidth and tokensPerPlayer
        have already been set or raises an ValueError
        '''
        if (limit * self.__fieldWidth) < self.__tokensPerPlayer:
            logger.debug("Tried to set too small limit=%d" % limit)
            raise ValueError("The limit is to small for the game conditions")
        self.__areaLanesLimit = limit
        
        
    @property
    def activePlayer(self):
        '''
        returns the player whos turn it is
        '''
        return self.__activePlayer
    
    @activePlayer.setter
    def activePlayer(self, player):
        '''
        this sets the player whos turn it is right now
        '''
        self.__activePlayer = player
        
    
    @property
    def playerCount(self):
        '''
        returns the playerCount
        '''
        return self.__playerCount
    
    @playerCount.setter
    def playerCount(self, playerCount):
        if playerCount != 2:
            logger.debug("Tried to set playercount != 2 in gameDataTwoPlayer")
            raise ValueError("Playercount can only be 2 in this gameData")
        self.__playerCount = playerCount
        
        
    @property
    def winner(self):
        '''
        returns the winner of the game
        '''
        return self.__winner
    
    @winner.setter
    def winner(self, player):
        '''
        sets the winner on one of the playing players
        '''
        if player == self.__playerOne or player == self.__playerTwo:
            self.__winner = player
        else:
            raise ValueError("The winning player is not part of the playing players")
        
        
    def nextGameState(self):
        '''
        increases the gamestate to the next state
        '''
        self.__gameState += 1
                
    def gameState(self):
        '''
        returns the current gameState
        '''
        return self.__gameState
    
    
