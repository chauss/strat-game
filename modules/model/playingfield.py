'''
Created on 29.03.2014

@author: Chris
'''
import logging.config
from . import field

logging.config.fileConfig('C:\\Users\\Chris\\git\\stratgame\\config\\log.config')
logger = logging.getLogger('model')

class PlayingField():
    def __init__(self, height, width):
        '''
        creates a new PlayingField object and sets its height and width
        '''
        self.__height = height
        self.__width = width
        logger.debug("Created a new PlayingField(id=%d)" % id(self))
        
    def build(self):
        self.__playingField = []
        for x in range(self.__height):
            self.__playingField[x].append([])
            for y in range(self.__width):
                self.__playingField[x].append(field.Field())
                logger.debug("Added Field(%d/%d) to PlayingField" % (x, y))
                
    def __str__(self):
        string = ""
        for x in range(self.__height):
            for y in range (self.__width):
                string += "["
                occToken = self.__playingField[x][y].getOccupyingToken()
                if occToken == None:
                    string += 4*" "
                else:
                    
                    string += ""