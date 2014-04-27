'''
Created on 29.03.2014

@author: Chris
'''
import logging.config
from field import Field
from myExceptions import PlayingFieldError
import ObserverPattern as ObserverPattern
from fieldToString import IFieldToString

logging.config.fileConfig('C:\\Users\\Chris\\git\\stratgame\\config\\log.config')
logger = logging.getLogger('controller')

class PlayingField(ObserverPattern.Subject):
    def __init__(self, gameData):
        '''
        creates a new PlayingField object and sets its height, width
        and the number of tokens for each player on this playingfield
        '''
        lanesPerPlayer = gameData.fieldHeight / gameData.playerCount
        fieldsPerPlayer = lanesPerPlayer * gameData.fieldWidth
        
        if fieldsPerPlayer >= gameData.tokensPerPlayer:
            super(PlayingField, self).__init__()
            self.__height = gameData.fieldHeight
            self.__width = gameData.fieldWidth
            self.__tokensPerPlayer = gameData.tokensPerPlayer
            self.__build = False
            self._build()
            self.__toString = IFieldToString()
            logger.debug("Created a new PlayingField(id=%d): %dX%d with %d tokens per player" % (id(self), self.__height, self.__width, self.__tokensPerPlayer))
        else:
            logger.debug("Tried to initialize a playingfield: %dX%d with %d tokens per player but only %d fields per player" % (gameData.fieldHeight(), gameData.fieldWidth(), gameData.tokensPerPlayer(), fieldsPerPlayer))
            raise ValueError("Not enough fields for that amount of tokens")
        
    def _build(self):
        '''
        this method will build the PlayingField, without being build
        the PlayingField can not be used
        '''
        self.__playingField = []
        for x in range(self.__height):
            self.__playingField.append([])
            for y in range(self.__width):
                self.__playingField[x].append(Field())
                logger.debug("Added Field(%d/%d) to PlayingField" % (x, y))
        self.__build = True
        
    def placeToken(self, token, x, y):
        '''
        tries to place the token on the field (x/y)
        if the PlayingField isn't build yet raises an PlayingFieldError
        if the field(x/y) is occupied raises an IllegalMoveError
        '''
        self.__playingField[x][y].moveTo(token)
        logger.debug("Placed token(id=%d) on PlayingField (%d/%d)" % (id(token), x, y))
        self.notify()
        
    def getTokenOnField(self, x, y):
        '''
        returns the token that occupies field x/y
        or None if there is no token on the field
        '''
        return self.__playingField[x][y].getOccupyingToken()
        
    def leaveField(self, x, y):
        '''
        deletes the token that sits on field x, y
        raises a PlayingFieldError if the field wasn't
        occupied
        '''
        if not self.__playingField[x][y].getOccupyingToken():
            logger.debug("Tried to leave field(%d/%d) but there is no token on it" % (x, y))
            raise PlayingFieldError("Can not leave an empty field")
        self.__playingField[x][y].leave()
        
    def setToString(self, toString):
        self.__toString = toString
        
    def __str__(self):
        return self.__toString.toString()
                