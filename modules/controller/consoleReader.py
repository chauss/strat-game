'''
Created on 04.04.2014

@author: Chris
'''
from gameDataTwoPlayer import TOKEN_PLACING, TOKEN_MOVING, \
                              GAME_FINISHED
from threading import Thread
import logging

logger = logging.getLogger('controller.consoleReader')
tui = logging.getLogger('tui.consoleReader')

class ConsoleReader(Thread):
    '''this class should be started in an extra thread.
    it waits for input from the command line
    '''
    def __init__(self, gameData, playingField, tokenPlacing, movement):
        Thread.__init__(self)
        self.__gameData = gameData
        self.__playingField = playingField
        self.__tokenPlacing = tokenPlacing
        self.__movement = movement
        self.__alive = True
        logger.debug("Created a new instance of ConsoleReader")
        
    def run(self):
        '''the method that is running as the thread
        '''
        logger.debug("Starting ConsoleReader...")
        while True:
            if self.__gameData.winner or not self.__alive:
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
                self.printAvailableCommands(gameState)
                
    def _tryToPlaceToken(self, myInput):
        '''tries to place a token if myInput has legal values
        '''
        if len(myInput) == 3:
            logger.debug("Calling tryToPlaceToken in tokenPlacing with args (%s, %s)" % (myInput[1], myInput[2]))
            self.__tokenPlacing.tryToPlaceToken(myInput[1], myInput[2])
        else:
            tui.info("Illegal input")
    
    def _tryToMoveToken(self, myInput):
        '''starts the movement of a token
        '''
        if len(myInput) == 5:
            logger.debug("Calling tryToMoveToken in movement with args: (%s, %s, %s, %s)" % (myInput[1], myInput[2], myInput[3], myInput[4]))
            self.__movement.tryToMoveToken(myInput[1], myInput[2], myInput[3], myInput[4])
        else:
            tui.info("Illegal input")
            
    def printAvailableCommands(self, gameState):
        '''logs the available commands with the tui logger
        '''
        if gameState == TOKEN_PLACING:
            tui.info("Available commands are: /place | /p")
        elif gameState == TOKEN_MOVING:
            tui.info("Available commands are: /move | /m")
            
    def shutdown(self):
        '''sets alive to False to break the while loop in run()
        '''
        self.__alive = False
                