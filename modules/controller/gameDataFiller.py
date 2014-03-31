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
    gameData.setFieldHeight(10)
    gameData.setFieldWidth(5)
    gameData.setTokensPerPlayer(10)
    gameData.setAreaLanesLimit(2)
    
    ab = AreaBuilder(gameData)
    ab.buildTopStartArea()
    ab.buildBottomStartArea()
    
    