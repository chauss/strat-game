'''
Created on 29.03.2014

@author: Chris
'''
from modules.controller.fieldToString import PlayerOnesTurn, PlayerTwosTurn
from modules.controller import utils
import logging.config

logging.config.fileConfig('C:\\Users\\Chris\\git\\stratgame\\config\\log.config')
logger = logging.getLogger('controller')
tui = logging.getLogger('tui')

class Movement():
    '''
    this class provides methods for a proper movement
    on a playingfield
    '''
    def __init__(self, playingField, gameData, movementRule):
        '''
        initializes the Movement object with the playingfield
        the movement should be done on
        '''
        self.__playingField = playingField
        self.__gameData = gameData
        self.__movementRule = movementRule
        self.__pot = PlayerOnesTurn(self.__playingField, self.__gameData)
        self.__ptt = PlayerTwosTurn(self.__playingField, self.__gameData)
        
    def tryToMoveToken(self, oldX, oldY, newX, newY):
        '''
        tries to move the token on field (oldX, oldY) to
        (newX, newY). also calculates the "fight"
        '''
        try:
            
            (oldX, oldY) = self._parseValuesToCoords(oldX, oldY)
            self._checkFieldIsOnPlayingField(oldX, oldY)
            
            (newX, newY) = self._parseValuesToCoords(newX, newY)
            self._checkFieldIsOnPlayingField(newX, newY)
            
            self.__movementRule.checkMove(oldX, oldY, newX, newY)
            
            player = self.__gameData.activePlayer()
            movingToken = self._getMovingToken(oldX, oldY)
            
            self._checkIfTokenBelongsToActivPlayer(movingToken, player)
            
            destiToken = self._getTokenOnDestinationField(newX, newY)
            
            if destiToken:
                self._checkIfTokenBelongsNotToActivPlayer(destiToken, player)
                self._fightAndMove(movingToken, oldX, oldY, destiToken, newX, newY)
            else:
                self.__playingField.leaveField(oldX, oldY)
                self.__playingField.placeToken(movingToken, newX, newY)
            
            self._changeTurn()
            
        except ValueError as e:
            tui.info(e)
            
    def _parseValuesToCoords(self, x, y):
        '''
        tries to parse the given x and y values into
        an integer
        '''
        try:
            x = int(x)
            y = int(y)
        except ValueError:
            logger.debug("User entered non int values: %s / %s" % (x, y))
            raise ValueError("Illegal coordinates: %s / %s" % (x, y))
        logger.debug("User entered int values: %d / %d" % (x, y))
        return (x, y)
    
    def _checkFieldIsOnPlayingField(self, x, y):
        '''
        checks weather the field x, y is on the playingfield
        or not
        '''
        height = self.__gameData.fieldHeight()
        width = self.__gameData.fieldWidth()
        
        if (x > height-1 or x < 0) or (y > width-1 or y < 0):
            raise ValueError("The coords (%d, %d) do not point on a field on the playingField" % (x, y))
        
    def _getMovingToken(self, x, y):
        '''
        returns the token on field x, y or raises an
        ValueError if there is no token on that field
        '''
        movingToken = self.__playingField.getTokenOnField(x, y)
        if not movingToken:
            logger.debug("Tried to move with token on field (%d, %d) but field is empty" % (x, y))
            raise ValueError("There is no token on field %d/%d to move" % (x, y))
        logger.debug("Could find a token on field (%d, %d)" % (x, y))
        return movingToken
    
    def _checkIfTokenBelongsToActivPlayer(self, token, player):
        '''
        checks if the tokens owner is player. if not so
        raises an ValueError
        '''
        if player != token.getOwner():
            logger.debug("Player %s tried to move with a token of player %s" % (player.getName(), token.getOwner().getName()))
            raise ValueError("The token you want to move with does belong to %s" % token.getOwner().getName())
        logger.debug("Check if the token to move with belongs to the active player passed: Belongs to %s" % player.getName())
        
    def _getTokenOnDestinationField(self, x, y):
        '''
        returns the token on the destination field or
        None if there is no token
        '''
        return self.__playingField.getTokenOnField(x, y)
    
    def _checkIfTokenBelongsNotToActivPlayer(self, token, player):
        '''
        checks if the player wants to move on a token that belongs
        to himself. if so raises an ValueError
        '''
        if player == token.getOwner():
            logger.debug("Player %s tried to move on his own token" % player.getName())
            raise ValueError("You can not move on your own token")
        logger.debug("Check if the token at moving destination belongs to active player passed")
    
    def _fightAndMove(self, movingToken, mx, my, destiToken, dx, dy):
        '''
        returns the surviving token. it does care for the
        losing token to be removed and checks if the player
        who lost a token has lost the game
        '''
        logger.debug("A fight broke out...")
        if destiToken.getRank() > movingToken.getRank():
            logger.debug("The movingToken lost: m(%d) < d(%d)" % (movingToken.getRank(), destiToken.getRank()))
            self.__playingField.leaveField(mx, my)
            movingToken.getOwner().removeTokenOnField(movingToken)
            if not movingToken.getOwner().getTokensOnField():
                self.__gameData.serWinner(destiToken.getOwner())
                self.__gameData.nextGameState()

        else:
            logger.debug("The destiToken lost: m(%d) >= d(%d)" % (movingToken.getRank(), destiToken.getRank()))
            self.__playingField.leaveField(mx, my)
            self.__playingField.leaveField(dx, dy)
            self.__playingField.placeToken(movingToken, dx, dy)
            destiToken.getOwner().removeTokenOnField(destiToken)
            if not destiToken.getOwner().getTokensOnField():
                self.__gameData.setWinner(movingToken.getOwner())
                self.__gameData.nextGameState()
                
    def _changeTurn(self):
        '''
        changes the active player and the to string method
        of the playingField
        '''
        logger.debug("Attempt to change turn...")
        activePlayer = self.__gameData.activePlayer()
        logger.debug("Active player is %s" % activePlayer.getName())
        
        if activePlayer == self.__gameData.playerOne():
            self.__gameData.setActivePlayer(self.__gameData.playerTwo())
            self.__playingField.setToString(self.__ptt)
            utils.changeTokenVisibility(self.__gameData.playerOne(), self.__gameData.playerTwo())
            
        else:
            self.__gameData.setActivePlayer(self.__gameData.playerOne())
            self.__playingField.setToString(self.__pot)
            utils.changeTokenVisibility(self.__gameData.playerTwo(), self.__gameData.playerOne())
            
        logger.debug("Changed active player to %s" % self.__gameData.activePlayer())
        self.__playingField.notify()
            
