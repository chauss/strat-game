'''
Created on 26.03.2014

@author: Chris
'''
import logging.config

from .myExceptions import InvalidRankError


logging.config.fileConfig('C:\\Users\\Chris\\git\\stratgame\\config\\log.config')
logger = logging.getLogger('model')
MIN_RANK = 1
MAX_RANK = 5

class Token():
    def __init__(self, rank, owner, revealed=True):
        '''
        Initializes a new token with the given rank
        and sets the revealed status to revealed (Default = True)
        owner is the owner of the token
        '''
        self.__rank = rank
        self.__owner = owner
        self.__revealed = revealed
        logger.debug("Created new token for player=%s with rank=%d and revealed=%r" % (self.__owner, rank, revealed))
        
    def setRank(self, newRank):
        '''
        sets the rank of the token to the newRank
        if newRank is within MIN_RANK and MAX_RANK
        or raises an InvalidRankException
        '''
        if(newRank < MIN_RANK or newRank > MAX_RANK):
            logger.debug("Tried to set tokens(id=%d) to invalid rank=%d, raising InvalidRankError" % (id(self), newRank))
            raise InvalidRankError(newRank)
        else:
            logger.debug("Set tokens(id=%d) rank to %d" % (id(self), newRank))
            self.__rank = newRank
        
    def getRank(self):
        '''
        returns the rank of the token
        can be within MIN_RANK and MAX_RANK
        '''
        return self.__rank
    
    def getOwner(self):
        '''
        returns the owner of the token
        '''
        return self.__owner
    
    def getVisibility(self):
        '''
        returns the visibility of the token
        can be True or False
        '''
        return self.__revealed
    
    def changeVisibility(self):
        '''
        inverses the visibility of the token
        from True to False or from False to True
        '''
        logger.debug("Changing tokens(id=%d) visibility from %r to %r" % (id(self), self.__revealed, not self.__revealed))
        self.__revealed = not self.__revealed
        
    def __str__(self):
        return "Token: rank=%d, id=%d" % (self.__rank, id(self))