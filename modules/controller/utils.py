'''
Created on 02.04.2014

@author: Chris
'''
import logging.config

logging.config.fileConfig('C:\\Users\\Chris\\git\\stratgame\\config\\log.config')
logger = logging.getLogger('controller')

def changeTokenVisibility(oldPlayer, newPlayer):
    for token in oldPlayer.getTokensOnField():
        token.changeVisibility()
    for token in newPlayer.getTokensOnField():
        token.changeVisibility()
    logger.debug("Changed %s tokens to invisible and %s tokens to visible" % (oldPlayer.getName(), newPlayer.getName()))