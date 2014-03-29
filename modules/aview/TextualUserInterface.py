'''
Created on 29.03.2014

@author: Chris
'''
import logging.config

logging.config.fileConfig('C:\\Users\\Chris\\git\\stratgame\\config\\log.config')
logger = logging.getLogger('tui')
                           
class Tui(object):
    def __init__(self, playingfield):
        self.__playingfield = playingfield
        self.__playingfield.build()
        self._print()
        
    def update(self):
        self._print()
        
    def _print(self):
        logger.info("%s" % str(self.__playingfield))