'''
Created on 29.03.2014

@author: Chris
'''
import unittest

from modules.controller import playingfield
from modules.model.token import Token
from modules.model import player
from modules.model.myExceptions import IllegalMoveError, PlayingFieldError
from modules.model.gameDataTwoPlayer import GameData

class PlayingFieldTest(unittest.TestCase):
    def testCreation(self):
        gd = GameData()
        gd.setFieldHeight(5)
        gd.setFieldWidth(5)
        gd.setTokensPerPlayer(10)
        pf = playingfield.PlayingField(gd)
        
    def testPlaceAndLeave(self):
        gd = GameData()
        gd.setFieldHeight(5)
        gd.setFieldWidth(5)
        gd.setTokensPerPlayer(10)
        pf = playingfield.PlayingField(gd)
        p = player.Player("TestPlayer", 1)
        t = Token(4, p)
        t2 = Token(5, p, False)
        pf.placeToken(t, 3, 3)
        pf.placeToken(t2, 0, 0)
        self.assertRaises(IllegalMoveError, pf.placeToken, t, 3, 3)
        self.assertEqual(pf.getTokenOnField(3, 3), t, "Token placed on a field is not returned correct")
        pf.leaveField(3, 3)
        self.assertEqual(pf.getTokenOnField(3, 3), None, "Token didn't left the field correct")
        self.assertRaises(PlayingFieldError, pf.leaveField, 3, 3)
        
        print str(pf)
    
    def testWrongInitialization(self):
        gd = GameData()
        gd.setFieldHeight(5)
        gd.setFieldWidth(5)
        gd.setTokensPerPlayer(13)
        self.assertRaises(ValueError, playingfield.PlayingField, gd)
        
        