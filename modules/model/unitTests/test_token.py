'''
Created on 27.03.2014

@author: Chris
'''
import unittest

from ..myExceptions import InvalidRankError
from .. import player
import my_token

class TokenTest(unittest.TestCase):
    
    def testCreateToken(self):
        p = player.Player("TestPlayer", 1)
        t = my_token.Token(1, p, True)
        self.assertEqual(t.getRank(), 1, "Rank wasn't initialized to 1 correctly")
        t.setRank(2)
        self.assertEqual(t.getRank(), 2, "Rank wasn't set to 2 correctly")
        
    def testGetOwner(self):
        p = player.Player("TestPlayer", 1)
        t = my_token.Token(1, p, True)
        self.assertEqual(t.getOwner(), p, "getOwner does not equal initialized owner")
    
    def testInvalidRank(self):
        p = player.Player("TestPlayer", 1)
        t = my_token.Token(1, p, True)
        self.assertRaises(InvalidRankError, t.setRank, (my_token.MAX_RANK+1))
        self.assertRaises(InvalidRankError, t.setRank, (my_token.MIN_RANK-1))
        
    def testVisibility(self):
        p = player.Player("TestPlayer", 1)
        t = my_token.Token(1, p, True)
        self.assertEqual(t.getVisibility(), True, "Visibility wasn't initilized to True correctly")
        t.changeVisibility()
        self.assertEqual(t.getVisibility(), False, "Visibility wasn't changed to False correctly")
        del t
        t = my_token.Token(1, p, False)
        self.assertEqual(t.getVisibility(), False, "Visibility wasn't initilized to False correctly")
        t.changeVisibility()
        self.assertEqual(t.getVisibility(), True, "Visibility wasn't changed to True correctly")


if __name__ == "__main__": 
    unittest.main()