'''
Created on 29.03.2014

@author: Chris
'''
import logging.config
from . import field
from .myExceptions import PlayingFieldError

logging.config.fileConfig('C:\\Users\\Chris\\git\\stratgame\\config\\log.config')
logger = logging.getLogger('model')

class PlayingField():
    def __init__(self, height, width):
        '''
        creates a new PlayingField object and sets its height and width
        '''
        self.__height = height
        self.__width = width
        self.__build = False
        logger.debug("Created a new PlayingField(id=%d)" % id(self))
        
    def build(self):
        '''
        this method will build the PlayingField, without being build
        the PlayingField can not be used
        '''
        self.__playingField = []
        for x in range(self.__height):
            self.__playingField.append([])
            for y in range(self.__width):
                self.__playingField[x].append(field.Field())
                logger.debug("Added Field(%d/%d) to PlayingField" % (x, y))
        self.__build = True
        
    def placeToken(self, token, x, y):
        '''
        tries to place the token on the field (x/y)
        if the PlayingField isn't build yet raises an PlayingFieldError
        if the field(x/y) is occupied raises an IllegalMoveError
        '''
        if self.__build:
            self.__playingField[x][y].moveTo(token)
        else:
            raise PlayingFieldError(self, "Need to run build() first")    
                
    def __str__(self):
        if self.__build:
            string = ""
            for x in range(self.__height):
                for y in range (self.__width):
                    string += "["
                    occToken = self.__playingField[x][y].getOccupyingToken()
                    if occToken == None:
                        string += 5*"-"
                    else:
                        playerID = occToken.getOwner().getIndex()
                        tokenRank = occToken.getRank()
                        string += "P%d(%d)" % (playerID, tokenRank)
                    string += "]"
                string += "\n"
        else:
            string = "PlayingField hasn't been build yet"
        return string
                