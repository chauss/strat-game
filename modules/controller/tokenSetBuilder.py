'''
Created on 01.04.2014

@author: Chris
'''
from token import MAX_RANK
import logging.config

logging.config.fileConfig('C:\\Users\\Chris\\git\\stratgame\\config\\log.config')
logger = logging.getLogger('controller')

def buildDefaultTokenSet(gameData):
    '''
    builds a list of token ranks that is used for
    the placing of the tokens in the beginning
    '''
    tokenSet = []
    for x in range(MAX_RANK+1):
        tokenSet.append(0)
    
    for x in range(gameData.tokensPerPlayer):
        tokenSet[x % (MAX_RANK+1)] += 1
        
    return tokenSet
    