'''
Created on 30.03.2014

@author: Chris
'''
import logging.config
import modules.util.ObserverPattern as ObserverPattern

logging.config.fileConfig('C:\\Users\\Chris\\git\\stratgame\\config\\log.config')
logger = logging.getLogger('controller')

class TokenPlacing(ObserverPattern.Subject):
    '''
    this class is for the first phase of a new game in which
    the tokens are placed on the PlayingField
    '''
    def __init__(self, playingField):
        self.__playingField = playingField
        
