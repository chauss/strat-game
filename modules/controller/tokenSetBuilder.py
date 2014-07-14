'''
Created on 01.04.2014

@author: Chris
'''
from my_token import MAX_RANK
import logging

logger = logging.getLogger('controller.tokensetBuilder')

def buildDefaultTokenSet(gameData):
    '''
    builds a list of my_token ranks that is used for
    the placing of the tokens in the beginning
    '''
    tokenSet = []
    for x in range(MAX_RANK+1):
        tokenSet.append(0)
    
    for x in range(gameData.tokensPerPlayer):
        tokenSet[x % (MAX_RANK+1)] += 1
        
    return tokenSet
    