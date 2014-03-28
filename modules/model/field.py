'''
Created on 27.03.2014

@author: Chris
'''
from myExceptions import IllegalMoveError
import logging.config
logging.config.fileConfig('C:\\Users\\Chris\\git\\stratgame\\config\\log.config')
logger = logging.getLogger('model')

class Field():
    '''
    This class represents a field of playing field
    '''
    def __init__(self):
        '''
        sets up a new field and initializes it with "unoccupied"
        '''
        self.__token = None
        logger.debug('Created new field with id=%d' % id(self))
        
    def isOccupied(self):
        '''
        returns the occupiing token or None if there is no token
        '''
        return self.__token
    
    def moveTo(self, token):
        '''
        if the field is unoccupied, the field save the coming token
        if the field is already occupied an IllegalMoveError is raised
        '''
        logger.debug("Token(id=%d) moved successfully to field(id=%d)" % (id(token), id(self)))
        if self.__token == None:
            self.__token = token
            logger.debug("Token(id=%d) moved successfully to field(id=%d)" % (id(token), id(self)))
        else:
            logger.debug("Token(id=%d) could not moveTo field(id=%d), raising IllegalMoveError" % (id(token), id(self)))
            raise IllegalMoveError(self)
    
    def leave(self):
        '''
        this will del the token who occupied the field
        if no token occupied the field nothing happens
        '''
        logger.debug("Leaving field(id=%d)" % id(self))
        self.__token = None
        
    def __str__(self):
        return "%d" % id(self)