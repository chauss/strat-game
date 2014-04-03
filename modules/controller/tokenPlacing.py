'''
Created on 30.03.2014

@author: Chris
'''
import logging.config
from modules.model.token import Token
import modules.util.ObserverPattern as ObserverPattern
from modules.controller.fieldToString import TokenPlacingStartArea
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
        
    def start(self):
        self._runPlayerPlacing(self.__gameData.playerOne())
        utils.changeTokenVisibility(self.__gameData.playerOne(), self.__gameData.playerTwo())
        tpsa = TokenPlacingStartArea(self.__playingField, self.__gameData, self.__gameData.bottomArea())
        self.__playingField.setToString(tpsa)
        self.__gameData.setActivePlayer(self.__gameData.playerTwo())
        
        self._runPlayerPlacing(self.__gameData.playerTwo())
        
    def _runPlayerPlacing(self, player):
        placedAll = 0
        placedRank = 0
        rank = 0
        
        while placedAll < self.__gameData.tokensPerPlayer():
            if self.__tokenSet[rank] > placedRank:
                token = Token(rank , player)
                self._tryToSetToken(token, player, rank)
                placedRank += 1
                placedAll += 1
            else:
                rank += 1
                placedRank = 0
                
    def _tryToSetToken(self, token, player, rank):
        '''
        tries to set a token on the field x, y that is asked
        from user
        starts again if there is already a token
        '''
        tokenPlaced = False
        
        while not tokenPlaced:
            (x, y) = self._getValidCoords(player, rank)
            occToken = self.__playingField.getTokenOnField(x, y)
            if occToken:
                tui.info("There is already a token on this field: (%d/%d)" % (x, y))
                continue
            self.__playingField.placeToken(token, x, y)
            player.addTokenOnField(token)
            tokenPlaced = True
        
    def _getValidCoords(self, player, rank):
        '''
        checks if the input coords from self._getValueFromUserToPlace
        are in his area:
        the top area is for the player with the index 1
        the bottom area is for the player with the index 2
        if the index of the player differs from that an valueError is raised
        '''
        if player.getIndex() == 1:
            area = self.__gameData.topArea()
        elif player.getIndex() == 2:
            area = self.__gameData.bottomArea()
        else:
            raise ValueError("The index of the player is not 1 or 2: %d" % player.getIndex())
        
        gotLegalCoords = False
        while not gotLegalCoords:
            x = self._getValueFromUserToPlace("x", rank, self.__gameData.fieldHeight())
            y = self._getValueFromUserToPlace("y", rank, self.__gameData.fieldWidth())
            
            if not area.isFieldInArea(x, y):
                tui.info("The given coords are not in your start area: (%d/%d)" % (x, y))
                continue
            gotLegalCoords = True
        
        return (x, y)

    def _getValueFromUserToPlace(self, value, tokenRank, maxValue):
        '''
        asks the player for the <value> coord to place a token with
        rank tokenRank and returns the coords
        '''
        Set = False
        while not Set:
            try:
                tui.info("Please enter %s value for token of rank %d: " % (value, tokenRank))
                val = int(raw_input(">>>>"))
                if val < 0 or val > maxValue:
                    raise
                Set = True
            except:
                tui.info("Please enter an int value between %d and %d" % (0, maxValue))
        logger.debug("Asked the user for %s coord and got %d" % (value, val))
        return val
    

        