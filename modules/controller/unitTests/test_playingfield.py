'''
Created on 29.03.2014

@author: Chris
'''
import unittest

from modules.controller import playingfield
from modules.model.token import Token
from modules.model import player
from modules.model.myExceptions import IllegalMoveError, PlayingFieldError

class PlayingFieldTest(unittest.TestCase):
    def testCreation(self):
        pf = playingfield.PlayingField(5, 5, 10)
        self.assertEqual(str(pf), "PlayingField hasn't been build yet", "PlayingField returns wrong string (testing if build yet No1)")
        pf.build()
        self.assertNotEqual(str(pf), "PlayingField hasn't been build yet", "PlayingField returns wrong string (testing if build yet No2)")
        
    def testPlaceToken(self):
        pf = playingfield.PlayingField(5, 5, 10)
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
        
    def testBuildTopArea(self):
        pf = playingfield.PlayingField(5, 5, 10)
        self.assertRaises(PlayingFieldError, pf.buildTopStartArea)
        pf.build()
        top = pf.buildTopStartArea()
        self.assertTrue(top.isFieldInArea(0, 0), "Top area does not contain first field (0/0)")
        self.assertTrue(top.isFieldInArea(1, 4), "Top area does not contain last field (1/4)")
        self.assertFalse(top.isFieldInArea(2, 0), "Top area contains to much fields")
        
        pf2 = playingfield.PlayingField(10, 10, 10)
        pf2.build()
        top2 = pf2.buildTopStartArea(1)
        self.assertTrue(top2.isFieldInArea(0, 0), "Top area does not contain first field (0/0)")
        self.assertTrue(top2.isFieldInArea(0, 9), "Top area does not contain last field (0/9)")
        self.assertFalse(top2.isFieldInArea(1, 0), "Top area contains to much fields")
        
        pf3 = playingfield.PlayingField(5, 5, 10)
        pf3.build()
        self.assertRaises(ValueError, pf3.buildTopStartArea, 1)
        
    def testBuildBottomArea(self):
        pf = playingfield.PlayingField(5, 5, 10)
        self.assertRaises(PlayingFieldError, pf.buildTopStartArea)
        pf.build()
        bot = pf.buildBottomStartArea()
        print bot
        self.assertTrue(bot.isFieldInArea(3, 0), "Bot area does not contain first field (3/0)")
        self.assertTrue(bot.isFieldInArea(4, 4), "Bot area does not contain last field (4/4)")
        self.assertFalse(bot.isFieldInArea(2, 4), "Bot area contains to much fields")
        
        pf2 = playingfield.PlayingField(10, 10, 10)
        pf2.build()
        bot2 = pf2.buildBottomStartArea(1)
        print bot2
        self.assertTrue(bot2.isFieldInArea(9, 0), "Bot area does not contain first field (0/0)")
        self.assertTrue(bot2.isFieldInArea(9, 9), "Bot area does not contain last field (0/9)")
        self.assertFalse(bot2.isFieldInArea(1, 0), "Bot area contains to much fields")
        
        pf3 = playingfield.PlayingField(5, 5, 10)
        pf3.build()
        self.assertRaises(ValueError, pf3.buildBottomStartArea, 1)
        
        
        