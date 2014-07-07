'''
Created on 02.04.2014

@author: Chris
'''
import logging

logger = logging.getLogger('controller.utils')

def changeTokenVisibility(oldPlayer, newPlayer):
    for token in oldPlayer.getTokensOnField():
        token.changeVisibility()
    for token in newPlayer.getTokensOnField():
        token.changeVisibility()
    logger.debug("Changed %s tokens to invisible and %s tokens to visible" % (oldPlayer.getName(), newPlayer.getName()))