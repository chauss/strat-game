'''
Created on 29.03.2014

@author: Chris
'''
import logging.config

logging.config.fileConfig('C:\\Users\\Chris\\git\\stratgame\\config\\log.config')
logger = logging.getLogger('model')

class Movement():
    '''
    this class provides methods for a proper movement
    on the playingfield
    '''
    def __init__(self, playingfield):
        '''
        initializes the Movement object with the playingfield
        the movement should be done on
        '''
        self.__playingfield = playingfield