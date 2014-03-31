'''
Created on 29.03.2014

@author: Chris
'''
import logging.config
from modules.model import field
from modules.model.myExceptions import PlayingFieldError
import modules.util.ObserverPattern as ObserverPattern
from modules.model.area import Area

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
        
    def buildTopStartArea(self, limit=False):
        '''
        builds the start area for the top of the field
        and returns it
        limit can be used to limit the area to less
        rows than the half of the game (if used must be an int)
        '''
        if not self.__build:
            logger.debug("Tried to build top area before building playingfield(id=%d)" % id(self))
            raise PlayingFieldError(self, "Need to run build() before building top area")
        
        topArea = Area()
        if not limit:
            lanes = self.__height / PLAYERS_PLAYING
            for x in range(lanes):
                for y in range(len(self.__playingField[x])):
                    topArea.addFieldCoords(x, y)
            logger.debug("Builded the top area for playingfield(id=%d) without limit" % id(self))
        else:
            if (limit * self.__width) < self.__tokensPerPlayer:
                logger.debug("Tried to build top area for playingfield(id=%d) with too small limit=%d" % (id(self), limit))
                raise ValueError("The limit is to hard for the game conditions")
            else:
                for x in range(limit):
                    for y in range(len(self.__playingField[x])):
                        topArea.addFieldCoords(x, y)
            logger.debug("Builded the top area for playingfield(id=%d) with limit=%d" % (id(self), limit))
        return topArea
    
    def buildBottomStartArea(self, limit=False):
        '''
        builds the start area for the bottom of the field
        and returns it
        limit can be used to limit the area to less
        rows than the half of the game (if used must be an int)
        '''
        if not self.__build:
            logger.debug("Tried to build bot area before building playingfield(id=%d)" % id(self))
            raise PlayingFieldError(self, "Need to run build() before building bot area")
        
        bottomArea = Area()
        if not limit:
            lanes = self.__height / PLAYERS_PLAYING
            start = self.__height - lanes
            end = self.__height
            for x in range(start, end):
                for y in range(len(self.__playingField[x])):
                    bottomArea.addFieldCoords(x, y)
            logger.debug("Builded the top area for playingfield(id=%d) without limit" % id(self))
        else:
            if (limit * self.__width) < self.__tokensPerPlayer:
                logger.debug("Tried to build bottom area for playingfield(id=%d) with too small limit=%d" % (id(self), limit))
                raise ValueError("The limit is to hard for the game conditions")
            else:
                lanes = self.__height / PLAYERS_PLAYING
                start = self.__height - limit
                end = self.__height
                for x in range(start, end):
                    for y in range(len(self.__playingField[x])):
                        bottomArea.addFieldCoords(x, y)
                logger.debug("Builded the bottom area for playingfield(id=%d) with limit=%d" % (id(self), limit))
        return bottomArea
                
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
                