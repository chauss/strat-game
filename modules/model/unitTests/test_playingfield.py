'''
Created on 29.03.2014

@author: Chris
'''
import unittest

from .. import playingfield
from .. import token
from .. import player
from ..myExceptions import IllegalMoveError

class PlayingFieldTest(unittest.TestCase):
    def testCreation(self):
        pf = playingfield.PlayingField(5,5)
        self.assertEqual(str(pf), "PlayingField hasn't been build yet", "PlayingField returns wrong string (testing if build yet No1)")
        pf.build()
        self.assertNotEqual(str(pf), "PlayingField hasn't been build yet", "PlayingField returns wrong string (testing if build yet No2)")
        
    def testPlaceToken(self):
        pf = playingfield.PlayingField(5,5)
        pf.build()
        p = player.Player("TestPlayer", 1)
        t = token.Token(4, p)
        pf.placeToken(t, 3, 3)
        self.assertRaises(IllegalMoveError, pf.placeToken, t, 3, 3)
        print str(pf)