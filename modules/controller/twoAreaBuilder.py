'''
Created on 31.03.2014

@author: Chris
'''
from modules.model.area import Area
import logging.config
import modules.model.gameDataTwoPlayer as gameDataTwoPlayer

logging.config.fileConfig('C:\\Users\\Chris\\git\\stratgame\\config\\log.config')
logger = logging.getLogger('controller')

class AreaBuilder(object):
    def __init__(self, gameData):
        if not isinstance(gameData, gameDataTwoPlayer):
            raise ValueError("Need an instance of gameData for two players")
        
        self.__gameData = gameData
        logger.debug("Created a new AreaBuilder(id=%d)" % id(self))
        
    def buildTopStartArea(self):
        '''
        builds the start area for the top of the field
        and saves it to the gameData
        '''
        topArea = Area()
        if not self.__gameData.AreaLanesLimit():
            lanes = self.__gameData.fieldHeight() / self.__gameData.playerCount()
            for x in range(lanes):
                for y in range(self.__gameData.fieldWidth()):
                    topArea.addFieldCoords(x, y)
            logger.debug("Builded the top area without limit")
        else:
            for x in range(self.__gameData.AreaLanesLimit()):
                for y in range(self.__gameData.fieldWidth):
                    topArea.addFieldCoords(x, y)
            logger.debug("Builded the top area with limit=%d" % self.__gameData.AreaLanesLimit())
        self.__gameData.setTopArea(topArea)
    
    def buildBottomStartArea(self):
        '''
        builds the start area for the bottom of the field
        and saves it to gameData
        '''
        bottomArea = Area()
        if not self.__gameData.AreaLanesLimit():
            lanes = self.__gameData.fieldHeight() / self.__gameData.playerCount()
            start = self.__gameData.fieldHeight() - lanes
            end = self.__gameData.fieldHeight()
            for x in range(start, end):
                for y in range(self.__gameData.fieldWidth()):
                    bottomArea.addFieldCoords(x, y)
            logger.debug("Builded the bottom area without limit")
        else:
            lanes = self.__height / self.__gameData.playerCount()
            start = self.__height - limit
            end = self.__height
            for x in range(start, end):
                for y in range(self.__gameData.fieldWidth()):
                    bottomArea.addFieldCoords(x, y)
            logger.debug("Builded the bottom area with limit=%d" % self.__gameData.AreaLanesLimit())
        self.__gameData.setBottomArea(bottomArea)