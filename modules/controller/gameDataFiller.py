'''
Created on 31.03.2014

@author: Chris
'''
from twoAreaBuilder import AreaBuilder
import logging

logger = logging.getLogger('controller.gameDataFiller')

def defaultGameDataTwoPlayer(gameData):
    '''
    fills the given gameData object with default
    game Data
    '''
    logger.debug("Filling gameData object with defaultGameDataTwoPlayer data")
    gameData.fieldHeight = 3
    gameData.fieldWidth = 1
    gameData.tokensPerPlayer = 1
    gameData.areaLanesLimit = 1
    
    ab = AreaBuilder(gameData)
    ab.buildTopStartArea()
    ab.buildBottomStartArea()
    
    