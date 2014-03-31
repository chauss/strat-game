'''
Created on 31.03.2014

@author: Chris
'''
import modules.model.gameDataTwoPlayer.GameData as GameData
import modules.controller.twoAreaBuilder.AreaBuilder as AreaBuilder
import logging.config

logging.config.fileConfig('C:\\Users\\Chris\\git\\stratgame\\config\\log.config')
logger = logging.getLogger('controller')

def defaultGameDataTwoPlayer(gameData):
    '''
    fills the given gameData object with default
    game Data
    '''
    if not isinstance(gameData, GameData):
        logger.debug("Tried to fill gameData in an object that is not instance of GameData")
        raise ValueError("gameData must be instance of GameData")
    gameData.setFieldHeight(10)
    gameData.setFieldWidth(5)
    gameData.setTokensPerPlayer(10)
    gameData.setAreaLanesLimit(2)
    
    ab = AreaBuilder(gameData)
    ab.buildTopStartArea()
    ab.buildBottomStartArea()
    
    