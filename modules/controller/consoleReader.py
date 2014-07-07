'''
Created on 04.04.2014

@author: Chris
'''
from gameDataTwoPlayer import TOKEN_PLACING, TOKEN_MOVING, \
                              GAME_FINISHED
from threading import Thread
import logging
import cmd

logger = logging.getLogger('controller.consoleReader')
tui = logging.getLogger('tui.consoleReader')

class ConsoleReader(Thread, cmd.Cmd):
    '''this class should be started in an extra thread.
    it waits for input from the command line
    '''
    def __init__(self, gameData, playingField, tokenPlacing, movement):
        cmd.Cmd.__init__(self)
        Thread.__init__(self)
        self.__gameData = gameData
        self.__playingField = playingField
        self.__tokenPlacing = tokenPlacing
        self.__movement = movement
        self.__alive = True
        self.prompt = ">>> "
        logger.debug("Created a new instance of ConsoleReader")
        
    def run(self):
        '''calls the run method of the command line (cmd.Cmd)
        '''
        logger.debug("Starting ConsoleReader...")
        self.cmdloop()
        logger.debug("Shutting down ConsoleReader")
        
###############################################################################
##------> Command methods
        
    # PLACE
    def do_p(self, prm):
        self.do_place(prm)
            
    def do_place(self, prm):
        '''checks the current gamestate and tries to place a token
        '''
        logger.debug("Read the input: %s" % prm)
        myInput = prm.split()
        gameState = self.__gameData.gameState()
        if gameState == TOKEN_PLACING:
            self._tryToPlaceToken(myInput)
        else:
            self.printUsage(gameState)
            
    def help_p(self):
        self.help_place()
            
    def help_place(self):
        tui.info('Help for command: place | p')
        tui.info('Available in GameState: TokenPlacing')
        tui.info('Needs two parameters:')
        tui.info('<xCoord> and <yCoord> of the field to place the token')
        tui.info('Example: place 0 0')
            
    # MOVE
    def do_m(self, prm):
        self.do_move(prm)
          
    def do_move(self, prm):
        '''checks the current gamestate and tries to move a token
        '''
        gameState = self.__gameData.gameState()
        myInput = prm.split()
        if gameState == TOKEN_MOVING:
            self._tryToMoveToken(myInput)
        else:
            self.printUsage(gameState)
            
    def help_m(self):
        self.help_move()
    
    def help_move(self):
        tui.info('Help for command: move | m')
        tui.info('Available in GameState: TokenMoving')
        tui.info('Needs four parameters:')
        tui.info('<xCoord> and <yCoord> of the tokens to walk with')
        tui.info('<xCoord> and <yCoord> of the field to walk to')
        tui.info('Example: move 0 0 0 1')
    
    # OTHER
    def emptyline(self):
        '''called when the user enters an empty line
        '''
        pass
    
    def default(self, prm):
        '''called when the user enters an unknown command
        '''
        tui.info('Unknown command: %s' % prm)
        tui.info('run \"help\" or \"help [command]\"')
        
    def do_EOF(self, prm):
        '''called when the user presses Strg + z
        '''
        return True
        
###############################################################################
##------> Work methods

    def printUsage(self, gameState):
        tui.info("This command is currently not available.")
        self.printAvailableCommands(gameState)
                
    def _tryToPlaceToken(self, myInput):
        '''tries to place a token if myInput has legal values
        '''
        if len(myInput) == 2:
            logger.debug("Calling tryToPlaceToken in tokenPlacing with args (%s, %s)" % (myInput[0], myInput[1]))
            self.__tokenPlacing.tryToPlaceToken(myInput[0], myInput[1])
        else:
            tui.info("Illegal input")
    
    def _tryToMoveToken(self, myInput):
        '''starts the movement of a token
        '''
        if len(myInput) == 4:
            logger.debug("Calling tryToMoveToken in movement with args: (%s, %s, %s, %s)" % (myInput[0], myInput[1], myInput[2], myInput[3]))
            self.__movement.tryToMoveToken(myInput[0], myInput[1], myInput[2], myInput[3])
        else:
            tui.info("Illegal input")
            
    def printAvailableCommands(self, gameState):
        '''logs the available commands with the tui logger
        '''
        tui.info("For more information about a command call \"help [command]\"")
        if gameState == TOKEN_PLACING:
            tui.info("Available commands are: place | p")
        elif gameState == TOKEN_MOVING:
            tui.info("Available commands are: move | m")
    
                