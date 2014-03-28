'''
Created on 27.03.2014

@author: Chris
'''
import unittest
import token
import player
from modules.myExceptions import InvalidRankError

class TokenTest(unittest.TestCase):
    
    def testCreateToken(self):
        p = player.Player("TestPlayer")
        t = token.Token(1, p, True)
        self.assertEqual(t.getRank(), 1, "Rank wasn't initialized to 1 correctly")
        t.setRank(2)
        self.assertEqual(t.getRank(), 2, "Rank wasn't set to 2 correctly")
    
    def testInvalidRank(self):
        p = player.Player("TestPlayer")
        t = token.Token(1, p, True)
        self.assertRaises(InvalidRankError, t.setRank, (token.MAX_RANK+1))
        self.assertRaises(InvalidRankError, t.setRank, (token.MIN_RANK-1))
        
    def testVisibility(self):
        p = player.Player("TestPlayer")
        t = token.Token(1, p, True)
        self.assertEqual(t.getVisibility(), True, "Visibility wasn't initilized to True correctly")
        t.changeVisibility()
        self.assertEqual(t.getVisibility(), False, "Visibility wasn't changed to False correctly")
        del t
        t = token.Token(1, p, False)
        self.assertEqual(t.getVisibility(), False, "Visibility wasn't initilized to False correctly")
        t.changeVisibility()
        self.assertEqual(t.getVisibility(), True, "Visibility wasn't changed to True correctly")


if __name__ == "__main__": 
    unittest.main()