'''
Created on 29.03.2014

@author: Chris
'''
import unittest

from modules.controller import playingfield
from modules.model.token import Token
from modules.model import player
from modules.model.myExceptions import IllegalMoveError

class PlayingFieldTest(unittest.TestCase):
    def testCreation(self):
        pf = playingfield.PlayingField(5, 5, 10)
        self.assertEqual(str(pf), "PlayingField hasn't been build yet", "PlayingField returns wrong string (testing if build yet No1)")
        pf.build()
        self.assertNotEqual(str(pf), "PlayingField hasn't been build yet", "PlayingField returns wrong string (testing if build yet No2)")
        
    def testPlaceToken(self):
        pf = playingfield.PlayingField(5, 5, 12)
        pf.build()
        p = player.Player("TestPlayer", 1)
        t = Token(4, p)
        t2 = Token(5, p, False)
        pf.placeToken(t, 3, 3)
        pf.placeToken(t2, 0, 0)
        self.assertRaises(IllegalMoveError, pf.placeToken, t, 3, 3)
        print str(pf)
    
    def testWrongInitialization(self):
        self.assertRaises(ValueError, playingfield.PlayingField, 5, 5, 13)
