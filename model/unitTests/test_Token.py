'''
Created on 27.03.2014

@author: Chris
'''
import unittest
import Token
from Exceptions import InvalidRankError

class TokenTest(unittest.TestCase):
    
    def testCreateToken(self):
        t = Token.Token(1, True)
        self.assertEqual(t.getRank(), 1, "Rank wasn't initialized to 1 correctly")
        t.setRank(2)
        self.assertEqual(t.getRank(), 2, "Rank wasn't set to 2 correctly")
    
    def testInvalidRank(self):
        t = Token.Token(1, True)
        self.assertRaises(InvalidRankError, t.setRank, (Token.MAX_RANK+1))
        self.assertRaises(InvalidRankError, t.setRank, (Token.MIN_RANK-1))
        
    def testVisibility(self):
        t = Token.Token(1, True)
        self.assertEqual(t.getVisibility(), True, "Visibility wasn't initilized to True correctly")
        t.changeVisibility()
        self.assertEqual(t.getVisibility(), False, "Visibility wasn't changed to False correctly")
        del t
        t = Token.Token(1, False)
        self.assertEqual(t.getVisibility(), False, "Visibility wasn't initilized to False correctly")
        t.changeVisibility()
        self.assertEqual(t.getVisibility(), True, "Visibility wasn't changed to True correctly")


if __name__ == "__main__": 
    unittest.main()