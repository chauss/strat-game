'''
Created on 27.03.2014

@author: Chris
'''
from Exceptions import IllegalMoveError

class Field():
    '''
    This class represents a field of playing field
    '''
    def __init__(self):
        '''
        sets up a new field and initializes it with "unoccupied"
        '''
        self.__occupied = False
        
    def getOccupiedStatus(self):
        '''
        returns the occupied state of the field
        '''
        return self.__occupied
    
    def moveTo(self):
        '''
        if the field is unoccupied, the field will be set occupied
        if the field is already occupied an IllegalMoveException is raised
        '''
        if not self.__occupied:
            self.__occupied = True
        else:
            raise IllegalMoveError(self)
        
    def __str__(self):
        return "%d" % id(self)