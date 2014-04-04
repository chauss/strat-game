'''
Created on 04.04.2014

@author: Chris
'''
from modules.model.gameDataTwoPlayer import TOKEN_PLACING, TOKEN_MOVING, \
                                            GAME_FINISHED
import logging.config

logging.config.fileConfig('C:\\Users\\Chris\\git\\stratgame\\config\\log.config')
logger = logging.getLogger('controller')
tui = logging.getLogger('tui')

class ConsoleReader(object):
    '''
    this class should be started in an extra thread.
    it waits for input from the textualuserinterface
    '''
    def __init__(self, gameData, playingField, tokenPlacing, movement):
        self.__gameData = gameData
        self.__playingField = playingField
        self.__tokenPlacing = tokenPlacing
        self.__movement = movement
        logger.debug("Starting ConsoleReader...")
        self._run()
        
    def _run(self):
        while True:
            myInput = raw_input()
            logger.debug("Read the input: %s" % myInput)
            if myInput[0] != '/':
                tui.info("Commands begin with a \"/\"")
                continue
            
            myInput = myInput.split()
            gameState = self.__gameData.gameState()
            if myInput[0] in ["/place", "/p"] and gameState == TOKEN_PLACING:
                self._tryToPlaceToken(myInput)
            elif myInput[0] in ["/move", "/m"] and gameState == TOKEN_MOVING:
                self._tryToMoveToken(myInput)
            else:
                tui.info("Not a legal command: %s" % myInput[0])
                
                
    def _tryToPlaceToken(self, myInput):
        '''
        tries to place a token if myInput has legal values
        '''
        if len(myInput) == 3:
            self.__tokenPlacing.tryToPlaceToken(myInput[1], myInput[2])
        else:
            tui.info("Illegal input")
    
    def _tryToMoveToken(self, myInput):
        pass
                
            
            
            
            
            
            