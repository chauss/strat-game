'''
Created on 02.04.2014

@author: Chris
'''
import logging.config

logging.config.fileConfig('C:\\Users\\Chris\\git\\stratgame\\config\\log.config')
logger = logging.getLogger('controller')

class IFieldToString(object):
    def toString(self, playingfield, gameData, area=None):
        raise NotImplementedError("Field to String method has not been set")
    
class PlayerOnesTurn(IFieldToString):
    def __init__(self, playingField, gameData, area=None):
        self.__playingField = playingField
        self.__gameData = gameData
        self.__area = area
        logger.debug("Created a new instance of PlayerOnesTurn-FieldPrinting")
    
    def toString(self):
        string = "   "
        for y in range(self.__gameData.fieldWidth()):
            string += "   %d   " % y
        string += "\n"
        for x in xrange(self.__gameData.fieldHeight()-1, -1, -1):
            string += "%d  " % x
            for y in range (self.__gameData.fieldWidth()):
                string += "["
                occToken = self.__playingField.getTokenOnField(x, y)
                if occToken == None:
                    string += 5*"-"
                else:
                    playerID = occToken.getOwner().getIndex()
                    if occToken.getVisibility():
                        tokenRank = occToken.getRank()
                        string += "P%d(%d)" % (playerID, tokenRank)
                    else:
                        string += "P%d(?)" % playerID
                string += "]"
            string += "\n"
        return string
    
    
class PlayerTwosTurn(IFieldToString):
    def __init__(self, playingField, gameData, area=None):
        self.__playingField = playingField
        self.__gameData = gameData
        self.__area = area
        logger.debug("Created a new instance of PlayerTwosTurn-FieldPrinting")
        
    def toString(self):
        string = "   "
        for y in range(self.__gameData.fieldWidth()):
            string += "   %d   " % y
        string += "\n"
        for x in range(self.__gameData.fieldHeight()):
            string += "%d  " % x
            for y in range (self.__gameData.fieldWidth()):
                string += "["
                occToken = self.__playingField.getTokenOnField(x, y)
                if occToken == None:
                    string += 5*"-"
                else:
                    playerID = occToken.getOwner().getIndex()
                    if occToken.getVisibility():
                        tokenRank = occToken.getRank()
                        string += "P%d(%d)" % (playerID, tokenRank)
                    else:
                        string += "P%d(?)" % playerID
                string += "]"
            string += "\n"
        return string
    
class TokenPlacingStartArea(IFieldToString):
    def __init__(self, playingField, gameData, area=None):
        self.__playingField = playingField
        self.__gameData = gameData
        self.__area = area
        logger.debug("Created a new instance of TokenPlacingStartArea-FieldPrinting")
    
    def toString(self):
        '''
        prints the playingfield with the starting area <area>
        specially marked 
        '''
        string = "   "
        for y in range(self.__gameData.fieldWidth()):
            string += "   %d   " % y
        string += "\n"
        for x in xrange(self.__gameData.fieldHeight()-1, -1, -1):
            string += "%d  " % x
            for y in range (self.__gameData.fieldWidth()):
                string += "["
                occToken = self.__playingField.getTokenOnField(x, y)
                if occToken == None:
                    if self.__area.isFieldInArea(x, y):
                        string += 5*'#'
                    else:
                        string += 5*"-"
                else:
                    playerID = occToken.getOwner().getIndex()
                    if occToken.getVisibility():
                        tokenRank = occToken.getRank()
                        string += "P%d(%d)" % (playerID, tokenRank)
                    else:
                        string += "P%d(?)" % playerID
                string += "]"
            string += "\n"
        return string
    