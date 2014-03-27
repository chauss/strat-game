'''
Created on 27.03.2014

@author: Chris
'''
from Exceptions import IllegalMoveError

class Field():
    def __init__(self):
        self.__occupied = False
        
    def getOccupiedStatus(self):
        return self.__occupied
    
    def moveTo(self):
        if not self.__occupied:
            self.__occupied = True
        else:
            raise IllegalMoveError(self)
        
    def __str__(self):
        return "%d" % id(self)