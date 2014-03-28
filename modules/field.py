'''
Created on 27.03.2014

@author: Chris
'''
from modules.myExceptions import IllegalMoveError
import logging.config
logging.config.fileConfig('..\\config\\log.config')
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
        
    def isOccupied(self):
        '''
        returns the occupiing token or None if the is no token
        '''
        return self.__token
    
    def moveTo(self, token):
        '''
        if the field is unoccupied, the field save the coming token
        if the field is already occupied an IllegalMoveError is raised
        '''
        if self.__token == None:
            self.__token = token
        else:
            raise IllegalMoveError(self)
    
    def leave(self):
        '''
        this will del the token who occupied the field
        if no token occupied the field nothing happens
        '''
        self.__token = None
        
    def __str__(self):
        return "%d" % id(self)