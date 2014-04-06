'''
Created on 31.03.2014

@author: Chris
'''
from modules.controller.twoAreaBuilder import AreaBuilder
import logging.config

logging.config.fileConfig('C:\\Users\\Chris\\git\\stratgame\\config\\log.config')
logger = logging.getLogger('controller')

def defaultGameDataTwoPlayer(gameData):
    '''
    fills the given gameData object with default
    game Data
    '''
    logger.debug("Filling gameData object with defaultGameDataTwoPlayer data")
    gameData.setFieldHeight(3)
    gameData.setFieldWidth(2)
    gameData.setTokensPerPlayer(2)
    gameData.setAreaLanesLimit(1)
    
    ab = AreaBuilder(gameData)
    ab.buildTopStartArea()
    ab.buildBottomStartArea()
    
    