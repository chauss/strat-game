'''
Created on 30.03.2014

@author: Chris
'''
import logging.config
from modules.model.token import Token
import modules.util.ObserverPattern as ObserverPattern
from modules.controller.fieldToString import TokenPlacingTopArea, TokenPlacingBottomArea, PlayerOnesTurn
from modules.controller import utils

logging.config.fileConfig('C:\\Users\\Chris\\git\\stratgame\\config\\log.config')
logger = logging.getLogger('controller')
tui = logging.getLogger('tui')

class TokenPlacing(ObserverPattern.Subject):
    '''
    this class is for the first phase of a new game in which
    the tokens are placed on the PlayingField
    '''
    def __init__(self, playingField, tokenSet, gameData):
        self.__playingField = playingField
        self.__tokenSet = tokenSet
        self.__gameData = gameData
        self.__gameData.setActivePlayer(self.__gameData.playerOne())
        tpta = TokenPlacingTopArea(self.__playingField, gameData)
        self.__playingField.setToString(tpta)
        self.__playingField.notify()
        
        self.__alreadyPlaced = 0
        self.__placedOfRank = 0
        self.__currentRank = 0
        
    def tryToPlaceToken(self, x, y):
        '''
        controls the try to set a token on field x, y
        '''
        logger.debug("Start to place a Token...")
        try:
            logger.debug("Enter While-loop check: tokenSet[currentRank(%d)](%d)  = placedOfRank(%d)" %(self.__currentRank, self.__tokenSet[self.__currentRank], self.__placedOfRank))
            while self.__tokenSet[self.__currentRank] == self.__placedOfRank:
                self.__currentRank += 1
                self.__placedOfRank = 0
                logger.debug("increased currentRank to %d" % self.__currentRank)

            (x, y) = self._parseValuesToCoords(x, y)
            
            area = self._getCurrentArea()
            self._checkValuesInArea(area, x, y)

            self._checkFieldIsEmpty(x, y)
            
            player = self.__gameData.activePlayer()
            token = Token(self.__currentRank, player)
            self.__playingField.placeToken(token, x, y)
            player.addTokenOnField(token)
            
            self.__placedOfRank += 1
            self.__alreadyPlaced += 1
            
            if self.__alreadyPlaced == self.__gameData.tokensPerPlayer():
                self.__currentRank = 0
                self.__placedOfRank = 0
                self.__alreadyPlaced = 0
                self._changePlayer()
            
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
        
    def _getCurrentArea(self):
        '''
        returns the current area depending on the player who
        is on turn
        '''
        player = self.__gameData.activePlayer()
        if player.getIndex() == 1:
            area = self.__gameData.topArea()
            logger.debug("Choosing topArea to place in")
        elif player.getIndex() == 2:
            area = self.__gameData.bottomArea()
            logger.debug("Choosing bottomArea to place in")
        return area
    
    def _checkValuesInArea(self, area, x, y):
        '''
        checks if the field x, y is in the area 
        '''
        if not area.isFieldInArea(x, y):
            logger.debug("Check if field is in area failed: Field is not in area")
            raise ValueError("The coordinates %d / %d are not in your area" % (x, y))
        logger.debug("Check if field is in area passed: Field is in area")
        
    def _checkFieldIsEmpty(self, x, y):
        '''
        checks weather the field is empty or a token
        is occupying it
        '''
        occToken = self.__playingField.getTokenOnField(x, y)
        if occToken:
            logger.debug("Check if field is empty failed: Field is occupied")
            raise ValueError("There is already a token on field %d / %d" % (x, y))
        logger.debug("Check if field is empty passed: Field is empty")
        
    def _changePlayer(self):
        '''
        changes the player to the next player or 
        ends the tokenPlacing state of the game
        '''
        logger.debug("Attempting to change Player...")
        player = self.__gameData.activePlayer()
        if player == self.__gameData.playerOne():
            logger.debug("activePlayer is PlayerOne: Changing to PlayerTwo")
            self.__gameData.setActivePlayer(self.__gameData.playerTwo())
            utils.changeTokenVisibility(self.__gameData.playerOne(), self.__gameData.playerTwo())
            tpba = TokenPlacingBottomArea(self.__playingField, self.__gameData)
            self.__playingField.setToString(tpba)
            self.__playingField.notify()
        else:
            logger.debug("Increasing gameState!")
            self.__gameData.nextGameState()
            pot = PlayerOnesTurn(self.__playingField, self.__gameData)
            self.__playingField.setToString(pot)
            self.__gameData.setActivePlayer(self.__gameData.playerOne())
            utils.changeTokenVisibility(self.__gameData.playerTwo(), self.__gameData.playerOne())
            self.__playingField.notify()
        
    