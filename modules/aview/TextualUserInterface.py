'''
Created on 29.03.2014

@author: Chris
'''
from modules.model.gameDataTwoPlayer import TOKEN_PLACING, TOKEN_MOVING, \
                                            GAME_FINISHED
import logging.config

logging.config.fileConfig('C:\\Users\\Chris\\git\\stratgame\\config\\log.config')
logger = logging.getLogger('tui')
                           
class Tui(object):
    def __init__(self, playingfield, gameData):
        self.__playingfield = playingfield
        self.__gameData = gameData
        
    def update(self):
        self._print()
        
    def _print(self):
        logger.info(80*">")
        logger.info(self._buildPlayerList)
        logger.info("%s" % str(self.__playingfield))
        logger.info(80*"<")
        logger.info(self._availableCommands)
        
    def _buildPlayerList(self):
        '''
        builds a string that contains the players and marks
        the player who is on turn right now
        '''
        logger.debug("Building PlayerList in GamesState: %d" % self.__gameData.gameState())
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
    
    def _availableCommands(self):
        '''
        prints the commands that are available in the current
        state of game
        '''
        commandString = ""
        gameState = self.gameData.gameState()
        if gameState == TOKEN_PLACING:
            commandString += "Available commands:\n"
            commandString += "/p or /place: <xCoord> <yCoord>\n"

        elif gameState == TOKEN_MOVING:
            commandString += "Available commands:\n"
            commandString += "/m or /move: <xCoordOld> <yCoordOld> <xCoordNew> <yCoordNew>\n"
            commandString += ">>>> "

        elif gameState == GAME_FINISHED:
            commandString += "The game is finished\n"
            commandString += ">>>> "

        return commandString
        