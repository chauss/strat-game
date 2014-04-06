'''
Created on 06.04.2014

@author: Chris
'''
import logging.config

logging.config.fileConfig('C:\\Users\\Chris\\git\\stratgame\\config\\log.config')
logger = logging.getLogger('controller')

class IMoveRule(object):
    def __init__(self):
        pass
    
    def checkMove(self, oldX, oldY, newX, newY):
        '''
        This is the method that decides weather a move can
        be done or not
        '''
        raise NotImplementedError()
    
class OneFieldPerMove(IMoveRule):
    def __init__(self):
        pass
    
    def checkMove(self, oldX, oldY, newX, newY):
        '''
        Checks if the field (oldX, oldY) is located
        beside the field (newX, newY) 
        '''
        checkPassed = False
        if newX == oldX + 1 or newX == oldX - 1:
            if newY == oldY:
                checkPassed = True
        elif newY == oldY + 1 or newY == oldY - 1:
            if newX == oldX:
                checkPassed = True
                
        if not checkPassed:
            raise ValueError("Not a legal move: you can only walk 1 field")
                
                