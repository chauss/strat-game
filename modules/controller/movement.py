'''
Created on 29.03.2014

@author: Chris
'''
from modules.model.myExceptions import IllegalMoveError
import logging.config

logging.config.fileConfig('C:\\Users\\Chris\\git\\stratgame\\config\\log.config')
logger = logging.getLogger('controller')

class Movement():
    '''
    this class provides methods for a proper movement
    on a playingfield
    '''
    def __init__(self, playingfield):
        '''
        initializes the Movement object with the playingfield
        the movement should be done on
        '''
        self.__playingfield = playingfield
        
    def moveFromTo(self, oldX, oldY, newX, newY, player):
        movingToken = self.__playingfield.getTokenOnField(oldX, oldY)
        if not movingToken:
            raise ValueError("There is no token on field %d/%d to move" % (oldX, oldY))
        elif player != movingToken.getOwner():
            raise IllegalMoveError("Player %s tried to move with a token of player %s" % (player.getName(), movingToken.getOwner().getName()))
                             
        destiToken = self.__playingfield.getTokenOnField(newX, newY)
        if destiToken: #if there is a token on the field movingToken wants to move
            
            #delete the movingToken if its rank is lower than the destiToken
            if destiToken.getRank() > movingToken.getRank():
                self.__playingfield.leaveField(oldX, oldY)
                player.removeTokenOnField(movingToken)
                return
            #else remove the destiToken and move to its position
            else:
                self.__playingfield.leaveField(newX, newY)
                self.__playingfield.leaveField(oldX, oldY)
                destiToken.getOwner().removeTokenOnField(destiToken)
                
                
        self.__playingfield.placeToken(movingToken, newX, newY)
                
        