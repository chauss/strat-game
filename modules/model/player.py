'''
Created on 28.03.2014

@author: Chris
'''
import logging.config
logging.config.fileConfig('..\\..\\config\\log.config')
logger = logging.getLogger('model')

class Player():
    def __init__(self, name):
        '''
        creates a new player which name is name
        '''
        self.__name = name
        logger.debug("Created new player with name=%s" % name)
        
    def getName(self):
        '''
        returns the name of the player
        '''
        return self.__name
        
    def __str__(self):
        return "%s" % self.__name