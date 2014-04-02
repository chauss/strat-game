'''
Created on 02.04.2014

@author: Chris
'''
import logging.config

logging.config.fileConfig('C:\\Users\\Chris\\git\\stratgame\\config\\log.config')
logger = logging.getLogger('controller')

class IFieldToString(object):
    def toString(self, playingfield):
        raise NotImplementedError("Field to String method has not been set")
    
class PlayerOnesTurn(IFieldToString):
    def toString(self, playingfield):
        
class PlayerTwosTurn(IFieldToString):
    def toString(self, playingfield):
        string = "   "
        for y in range(self.__width):
            string += "   %d   " % y
        string += "\n"
        for x in range(self.__height):
            string += "%d  " % x
            for y in range (self.__width):
                string += "["
                occToken = self.__playingField[x][y].getOccupyingToken()
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
    
class TokenPlacingPlayerOne(IFieldToString):
    def toString(self, playingfield):
        
class TokenPlacingPlayerTwo(IFieldToString):
    def toString(self, playingfield):