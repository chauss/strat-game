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
    gameData.fieldHeight = 4
    gameData.fieldWidth = 1
    gameData.tokensPerPlayer = 1
    gameData.areaLanesLimit = 1
    
    ab = AreaBuilder(gameData)
    ab.buildTopStartArea()
    ab.buildBottomStartArea()
    
    