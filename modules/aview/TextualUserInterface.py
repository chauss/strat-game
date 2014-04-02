'''
Created on 29.03.2014

@author: Chris
'''
import logging.config

logging.config.fileConfig('C:\\Users\\Chris\\git\\stratgame\\config\\log.config')
logger = logging.getLogger('tui')
                           
class Tui(object):
    def __init__(self, playingfield, gameData):
        self.__playingfield = playingfield
        self.__gameData = gameData
        self.__playerList = self._buildPlayerList()
        self._print()
        
    def update(self):
        self._print()
        
    def _print(self):
        logger.info(80*">")
        logger.info(self.__playerList)
        logger.info("%s" % str(self.__playingfield))
        logger.info(80*"<")
        
    def _buildPlayerList(self):
        pList = ""
        playerOne = self.__gameData.playerOne()
        playerTwo = self.__gameData.playerTwo()
        activePlayer = self.__gameData.activePlayer()
        
        if playerOne == activePlayer:
            pList += "P%d: %s <<<<\n" % (playerOne.getIndex(), playerOne.getName())
            pList += "P%d: %s\n" % (playerTwo.getIndex(), playerTwo.getName())
        else:
            pList += "P%d: %s\n" % (playerOne.getIndex(), playerOne.getName())
            pList += "P%d: %s <<<<\n" % (playerTwo.getIndex(), playerTwo.getName())
        return pList
        