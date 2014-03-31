'''
Created on 30.03.2014

@author: Chris
'''
import logging.config

logging.config.fileConfig('C:\\Users\\Chris\\git\\stratgame\\config\\log.config')
logger = logging.getLogger('model')

class Area(object):
    def __init__(self):
        '''
        initializes an area of a playingfield
        '''
        self.__area = []
        logger.debug("Created a new Area(id=%d)" % id(self))
        
    def addFieldCoords(self, x, y):
        '''
        adds the coords x,y to the area
        '''
        if not (x, y) in self.__area:
            self.__area.append((x,y))
            logger.debug("Added coords (%d/%d) to area(id=%d)" % (x, y, id(self)))
        
    def delFieldCoords(self, x, y):
        '''
        deletes the coords x,y from the area if they are
        in the selection
        '''
        try:
            logger.debug("Trying to remove coords (%d/%d) from area(id=%d)" % (x, y, id(self)))
            self.__area.remove((x, y))
        except ValueError:
            logger.debug("Couldn't remove coords (%d/%d) from area(id=%d): They are not in the area" % (x, y, id(self)))
        
    def isFieldInArea(self, x, y):
        '''
        returns True if (x, y) is in the area or False if not
        '''
        if (x, y) in self.__area:
            logger.debug("Checking if coords (%d/%d) are in area(id=%d): True" % (x, y, id(self)))
            return True
        logger.debug("Checking if coords (%d/%d) are in area(id=%d): False" % (x, y, id(self)))
        return False
    
    def __str__(self):
        string = ""
        for x in self.__area:
            string += "(%d/%d)\n" % x
        return string
    
    