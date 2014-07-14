'''
Created on 13.04.2014

@author: Chris
'''
import pygame
from pygame.locals import *
from playingfield import PlayingField
from gameDataTwoPlayer import GameData
from gameDataFiller import defaultGameDataTwoPlayer
from player import Player

FIELD_SIZE = 10

pygame.init()

def buildPlayingFieldSurface(pf, gD):
    '''
    creates out of the given playingField pf
    a gui for the playingField (a surface)
    need gameData gD for information about the 
    playingField
    '''
    pf = pygame.Surface( (FIELD_SIZE * gD.fieldHeight(), FIELD_SIZE * gD.fieldWidth()) )
    
    for x in range(gD.fieldHeight()):
        for y in range(gD.fieldWidth()):
            gf = GuiField(x, y)
            pf.blit(gf, (x * FIELD_SIZE, y * FIELD_SIZE))
    
    return pf
            
            
    
class GuiField(object):
    def __init__(self, x, y):
        self._rect = pygame.Rect(x, y, FIELD_SIZE, FIELD_SIZE)
        self._x = x
        self._y = y

gameData = GameData()
defaultGameDataTwoPlayer(gameData)

gameData.setPlayerOne(Player("Chris", 1))
gameData.setPlayerTwo(Player("Laura", 2))

pf = PlayingField(gameData)
pf_gui = buildPlayingFieldSurface(pf, gameData)

screen = pygame.display.set_mode((800, 600))

screen.blit(pf_gui, (40, 40))
