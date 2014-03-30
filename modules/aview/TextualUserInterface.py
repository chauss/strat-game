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
        self._print()
        
    def update(self):
        self._print()
        
    def _print(self):
        logger.info(80*">")
        logger.info("%s" % str(self.__playingfield))
        logger.info(80*"<")
        
    def _buildPlayerList(self):
        pass