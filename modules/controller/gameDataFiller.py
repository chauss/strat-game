'''
Created on 31.03.2014

@author: Chris
'''
from twoAreaBuilder import AreaBuilder
import logging.config

logging.config.fileConfig('C:\\Users\\Chris\\git\\stratgame\\config\\log.config')
logger = logging.getLogger('controller')

def defaultGameDataTwoPlayer(gameData):
    '''
    fills the given gameData object with default
    game Data
    '''
    logger.debug("Filling gameData object with defaultGameDataTwoPlayer data")
    gameData.fieldHeight = 10
    gameData.fieldWidth = 5
    gameData.tokensPerPlayer = 10
    gameData.areaLanesLimit = 2
    
    ab = AreaBuilder(gameData)
    ab.buildTopStartArea()
    ab.buildBottomStartArea()
    
    