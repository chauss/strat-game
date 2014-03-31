'''
Created on 29.03.2014

@author: Chris
'''
import logging.config
from modules.model import field
from modules.model.myExceptions import PlayingFieldError
import modules.util.ObserverPattern as ObserverPattern

logging.config.fileConfig('C:\\Users\\Chris\\git\\stratgame\\config\\log.config')
logger = logging.getLogger('controller')

PLAYERS_PLAYING = 2

class PlayingField(ObserverPattern.Subject):
    def __init__(self, height, width, tokensPerPlayer):
        '''
        creates a new PlayingField object and sets its height, width
        and the number of tokens for each player on this playingfield
        '''
        lanesPerPlayer = height / PLAYERS_PLAYING
        fieldsPerPlayer = lanesPerPlayer * width
        
        if fieldsPerPlayer >= tokensPerPlayer:
            super(PlayingField, self).__init__()
            self.__height = height
            self.__width = width
            self.__tokensPerPlayer = tokensPerPlayer
            self.__build = False
            logger.debug("Created a new PlayingField(id=%d): %dX%d with %d tokens per player" % (id(self), height, width, tokensPerPlayer))
        else:
            logger.debug("Tried to initialize a playingfield: %dX%d with %d tokens per player but only %d fields per player" % (height, width, tokensPerPlayer, fieldsPerPlayer))
            raise ValueError("Not enough fields for that amount of tokens")
        
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
            logger.debug("Placed token(id=%d) on PlayingField (%d/%d)" % (id(token), x, y))
            self.notify()
        else:
            logger.debug("Tried to place token(id=%d) on not builded Playingfield(id=%d) on (%d/%d)" % (id(token), id(self), x, y))
            raise PlayingFieldError(self, "Need to run build() first")
        
    def __str__(self):
        if self.__build:
            string = "   "
            for y in range(self.__width):
                string += "   %d   " % y
            string += "\n"
            for x in range(self.__height):
                string += "%d  " % x
                for y in range (self.__width):
                    string += "["
                    occToken = self.__playingField[x][y].getOccupyingToken()
                    if occToken == None:
                        string += 5*"-"
                    else:
                        playerID = occToken.getOwner().getIndex()
                        if occToken.getVisibility():
                            tokenRank = occToken.getRank()
                            string += "P%d(%d)" % (playerID, tokenRank)
                        else:
                            string += "P%d(?)" % playerID
                    string += "]"
                string += "\n"
        else:
            string = "PlayingField hasn't been build yet"
        return string
                