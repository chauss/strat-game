'''
Created on 29.03.2014

@author: Chris
'''
from gameDataTwoPlayer import TOKEN_PLACING, TOKEN_MOVING, \
                                            GAME_FINISHED
import logging

logger = logging.getLogger('tui')
                           
class Tui(object):
    def __init__(self, playingfield, gameData):
        self.__playingfield = playingfield
        self.__gameData = gameData
        
    def update(self):
        self._print()
        
    def _print(self):
        logger.info(80*">")
        logger.info(self._buildPlayerList())
        logger.info(self._gameState())
        logger.info("%s" % str(self.__playingfield))
        logger.info(80*"<")
        
    def _buildPlayerList(self):
        '''
        builds a string that contains the players and marks
        the player who is on turn right now
        '''
        logger.debug("Building PlayerList in GameState: %d" % self.__gameData.gameState())
        pList = ""
        playerOne = self.__gameData.playerOne
        playerTwo = self.__gameData.playerTwo
        activePlayer = self.__gameData.activePlayer
        
        if playerOne == activePlayer:
            pList += "P%d: %s <<<<\n" % (playerOne.getIndex(), playerOne.getName())
            pList += "P%d: %s\n" % (playerTwo.getIndex(), playerTwo.getName())
        else:
            pList += "P%d: %s\n" % (playerOne.getIndex(), playerOne.getName())
            pList += "P%d: %s <<<<\n" % (playerTwo.getIndex(), playerTwo.getName())
        return pList
    
    def _gameState(self):
        '''
        returns a string that shows the current gameState
        '''
        string = "Current gameState: "
        currentGameState = self.__gameData.gameState()
        if currentGameState == TOKEN_PLACING:
            string += "Token Placing"
        elif currentGameState == TOKEN_MOVING:
            string += "Token Moving"
        elif currentGameState == GAME_FINISHED:
            string += "Game Finished: Winner is %s" % self.__gameData.winner.getName()
        return string
    
        