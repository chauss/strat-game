'''
Created on 26.03.2014

@author: Chris
'''
from Exceptions import InvalidRankError
MIN_RANK = 1
MAX_RANK = 5

class Token():
    def __init__(self, rank, revealed=True):
        '''
        Initializes a new token with the given rank
        and sets the revealed status to revealed (Default = True)
        '''
        self.__rank = rank
        self.__revealed = revealed
        
    def setRank(self, newRank):
        '''
        sets the rank of the token to the newRank
        if newRank is within MIN_RANK and MAX_RANK
        or raises an InvalidRankException
        '''
        if(newRank < MIN_RANK or newRank > MAX_RANK):
            raise InvalidRankError(newRank)
        else:
            self.__rank = newRank
        
    def getRank(self):
        '''
        returns the rank of the token
        can be within MIN_RANK and MAX_RANK
        '''
        return self.__rank
    
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
        self.__revealed = not self.__revealed
        
    def __str__(self):
        return "Token: rank=%d, id=%d" % (self.__rank, id(self))