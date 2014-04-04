'''
Created on 04.04.2014

@author: Chris
'''
import logging.config

logging.config.fileConfig('C:\\Users\\Chris\\git\\stratgame\\config\\log.config')
logger = logging.getLogger('controller')
tui = logging.getLogger('tui')

class ConsoleReader(object):
    '''
    this class should be started in an extra thread.
    it waits for input from the textualuserinterface
    '''
    def __init__(self, gameData, playingField):
        self.__gameData = gameData
        self.__playingField = playingField
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
            if myInput[0] in ["/place", "/p"]:
                self._tryToPlaceToken(myInput)
            elif myInput[0] in ["/move", "/m"]:
                self._tryToMoveToken(myInput)
            else:
                tui.info("Not a legal command: %s" % myInput[0])
                
                
    def _tryToPlaceToken(self, myInput):
        '''
        tries to place a token if myInput has legal values
        '''
        
    def _tryToMoveToken(self, myInput):
        
                
            
            
            
            
            
            