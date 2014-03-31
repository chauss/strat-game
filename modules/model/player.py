'''
Created on 28.03.2014

@author: Chris
'''
import logging.config

logging.config.fileConfig('C:\\Users\\Chris\\git\\stratgame\\config\\log.config')
logger = logging.getLogger('model')

class Player():
    def __init__(self, name, index):
        '''
        creates a new player which name is name
        with an index that should be unique
        '''
        self.__name = name
        self.__index = index
        logger.debug("Created new player with name=%s" % name)
        
    def getName(self):
        '''
        returns the name of the player
        '''
        return self.__name
    
    def getIndex(self):
        '''
        returns the index of the player
        '''
        return self.__index
        
    def __str__(self):
        return "%s" % self.__name