'''
Created on 04.04.2014

@author: Chris
'''
from gameDataTwoPlayer import TOKEN_PLACING, TOKEN_MOVING
from threading import Thread
import logging
import gamemaster as gm
import cmd
from mainframeapp import MainWindow
import wx

logger = logging.getLogger('controller.consoleReader')
tui = logging.getLogger('tui.consoleReader')

class ConsoleReader(Thread, cmd.Cmd):
    '''this class should be started in an extra thread.
    it waits for input from the command line
    '''
    def __init__(self):
        cmd.Cmd.__init__(self)
        Thread.__init__(self)
        self.__game = None
        self.__gameData = None
        self.__playingField = None
        self.__tokenPlacing = None
        self.__movement = None
        self.__alive = True
        self.app = wx.App(False)
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
        
    # Start GUI
    def do_startx(self, prm):
        '''starts the gui'''
        frame = MainWindow(None, self.__gameData)
        frame.Show()
        self.app.MainLoop()
    
    # Start a game
    def do_start(self, prm):
        '''starts the game, if not given any values the default values
        are taken
        '''
        self.__game = gm.TwoManGame()
        (self.__gameData, self.__playingField, self.__tokenPlacing, self.__movement) \
        = self.__game.getGameDatas()
        self.__gameData.nextGameState()
        
    # PLACE
    def do_p(self, prm):
        self.do_place(prm)
            
    def do_place(self, prm):
        '''checks the current gamestate and tries to place a my_token
        '''
        if not (self.__gameData and self.__gameData.gameState() == TOKEN_PLACING):
            self.printUsage()
            return
            
        logger.debug("Read the input: %s" % prm)
        myInput = prm.split()
        self._tryToPlaceToken(myInput)
            
            
    def help_p(self):
        self.help_place()
            
    def help_place(self):
        tui.info('Help for command: place | p')
        tui.info('Available in GameState: TokenPlacing')
        tui.info('Needs two parameters:')
        tui.info('<xCoord> and <yCoord> of the field to place the my_token')
        tui.info('Example: place 0 0')
            
    # MOVE
    def do_m(self, prm):
        self.do_move(prm)
          
    def do_move(self, prm):
        '''checks the current gamestate and tries to move a my_token
        '''
        if not (self.__gameData and self.__gameData.gameState() == TOKEN_MOVING):
            self.printUsage()
            return
            
        myInput = prm.split()
        self._tryToMoveToken(myInput)

            
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

    def printUsage(self):
        tui.info("This command is currently not available.")
        self.printAvailableCommands()
                
    def _tryToPlaceToken(self, myInput):
        '''tries to place a my_token if myInput has legal values
        '''
        if len(myInput) == 2:
            logger.debug("Calling tryToPlaceToken in tokenPlacing with args (%s, %s)" % (myInput[0], myInput[1]))
            self.__tokenPlacing.tryToPlaceToken(myInput[0], myInput[1])
        else:
            tui.info("Illegal input")
    
    def _tryToMoveToken(self, myInput):
        '''starts the movement of a my_token
        '''
        if len(myInput) == 4:
            logger.debug("Calling tryToMoveToken in movement with args: (%s, %s, %s, %s)" % (myInput[0], myInput[1], myInput[2], myInput[3]))
            self.__movement.tryToMoveToken(myInput[0], myInput[1], myInput[2], myInput[3])
        else:
            tui.info("Illegal input")
            
    def printAvailableCommands(self):
        '''logs the available commands with the tui logger
        '''
        gameState = None
        if self.__gameData:
            gameState = self.__gameData.gameState()
        tui.info("For more information about a command call \"help [command]\"")
        if not gameState:
            tui.info("Available commands are: start")
        elif gameState == TOKEN_PLACING:
            tui.info("Available commands are: place | p")
        elif gameState == TOKEN_MOVING:
            tui.info("Available commands are: move | m")
    
                