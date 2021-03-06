'''
Created on 28.03.2014

@author: Chris
'''
import logging

logger = logging.getLogger('model.player')

class Player():
    def __init__(self, name, index):
        '''
        creates a new player which name is name
        with an index that should be unique
        '''
        self.__name = name
        self.__index = index
        self.__tokensOnField = []
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
    
    def addTokenOnField(self, token):
        '''
        adds a my_token to the players tokens on the field
        '''
        self.__tokensOnField.append(token)
        
    def getTokensOnField(self):
        '''
        returns a list of the tokens on field of this player
        '''
        return self.__tokensOnField
        
        
    def removeTokenOnField(self, token):
        '''
        removes a my_token of the player from the list of its
        tokens on the field
        '''
        if token in self.__tokensOnField:
            self.__tokensOnField.remove(token)
        else:
            raise ValueError("Token is not in players list: can not remove it")
        
    def __str__(self):
        return "%s" % self.__name