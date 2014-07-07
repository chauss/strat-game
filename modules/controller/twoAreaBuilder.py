'''
Created on 31.03.2014

@author: Chris
'''
from area import Area
import logging

logger = logging.getLogger('controller.2areaBuilder')

class AreaBuilder(object):
    def __init__(self, gameData):
        self.__gameData = gameData
        logger.debug("Created a new AreaBuilder(id=%d)" % id(self))
        
    def buildTopStartArea(self):
        '''
        builds the start area for the top of the field
        and saves it to the gameData
        '''
        topArea = Area()
        if not self.__gameData.areaLanesLimit:
            lanes = self.__gameData.fieldHeight / self.__gameData.playerCount
            for x in range(lanes):
                for y in range(self.__gameData.fieldWidth):
                    topArea.addFieldCoords(x, y)
            logger.debug("Builded the top area without limit")
        else:
            for x in range(self.__gameData.areaLanesLimit):
                for y in range(self.__gameData.fieldWidth):
                    topArea.addFieldCoords(x, y)
            logger.debug("Builded the top area with limit=%d" % self.__gameData.areaLanesLimit)
        self.__gameData.topArea = topArea
    
    def buildBottomStartArea(self):
        '''
        builds the start area for the bottom of the field
        and saves it to gameData
        '''
        bottomArea = Area()
        if not self.__gameData.areaLanesLimit:
            lanes = self.__gameData.fieldHeight / self.__gameData.playerCount
            start = self.__gameData.fieldHeight - lanes
            end = self.__gameData.fieldHeight
            for x in range(start, end):
                for y in range(self.__gameData.fieldWidth):
                    bottomArea.addFieldCoords(x, y)
            logger.debug("Builded the bottom area without limit")
        else:
            lanes = self.__gameData.fieldHeight / self.__gameData.playerCount
            start = self.__gameData.fieldHeight - self.__gameData.areaLanesLimit
            end = self.__gameData.fieldHeight
            for x in range(start, end):
                for y in range(self.__gameData.fieldWidth):
                    bottomArea.addFieldCoords(x, y)
            logger.debug("Builded the bottom area with limit=%d" % self.__gameData.areaLanesLimit)
        self.__gameData.bottomArea = bottomArea