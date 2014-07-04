'''
Created on 04.04.2014

@author: Chris
'''
from gameDataTwoPlayer import TOKEN_PLACING, TOKEN_MOVING, \
                              GAME_FINISHED
from threading import Thread
import logging.config

logging.config.fileConfig('C:\\Users\\Chris\\git\\stratgame\\config\\log.config')
logger = logging.getLogger('controller')
tui = logging.getLogger('tui')

class ConsoleReader(Thread):
    '''
    this class should be started in an extra thread.
    it waits for input from the textualuserinterface
    '''
    def __init__(self, gameData, playingField, tokenPlacing, movement):
        Thread.__init__(self)
        self.__gameData = gameData
        self.__playingField = playingField
        self.__tokenPlacing = tokenPlacing
        self.__movement = movement
        logger.debug("Created a new instance of ConsoleReader")
        
    def run(self):
        logger.debug("Starting ConsoleReader...")
        while True:
            if self.__gameData.winner:
                logger.debug("Shutting down ConsoleReader")
                break
            
            myInput = raw_input(">>>> ")
            logger.debug("Read the input: %s" % myInput)
            if not myInput or myInput[0] != '/':
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
            logger.debug("Calling tryToPlaceToken in tokenPlacing with args (%s, %s)" % (myInput[1], myInput[2]))
            self.__tokenPlacing.tryToPlaceToken(myInput[1], myInput[2])
        else:
            tui.info("Illegal input")
    
    def _tryToMoveToken(self, myInput):
        '''
        starts the movement of a token
        '''
        if len(myInput) == 5:
            logger.debug("Calling tryToMoveToken in movement with args: (%s, %s, %s, %s)" % (myInput[1], myInput[2], myInput[3], myInput[4]))
            self.__movement.tryToMoveToken(myInput[1], myInput[2], myInput[3], myInput[4])
        else:
            tui.info("Illegal input")
                
            
            
            
            
            
            