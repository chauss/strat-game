'''
Created on 27.03.2014

@author: Chris
'''
import unittest
import token
from modules.myExceptions import InvalidRankError

class TokenTest(unittest.TestCase):
    
    def testCreateToken(self):
        t = token.Token(1, True)
        self.assertEqual(t.getRank(), 1, "Rank wasn't initialized to 1 correctly")
        t.setRank(2)
        self.assertEqual(t.getRank(), 2, "Rank wasn't set to 2 correctly")
    
    def testInvalidRank(self):
        t = token.Token(1, True)
        self.assertRaises(InvalidRankError, t.setRank, (token.MAX_RANK+1))
        self.assertRaises(InvalidRankError, t.setRank, (token.MIN_RANK-1))
        
    def testVisibility(self):
        t = token.Token(1, True)
        self.assertEqual(t.getVisibility(), True, "Visibility wasn't initilized to True correctly")
        t.changeVisibility()
        self.assertEqual(t.getVisibility(), False, "Visibility wasn't changed to False correctly")
        del t
        t = token.Token(1, False)
        self.assertEqual(t.getVisibility(), False, "Visibility wasn't initilized to False correctly")
        t.changeVisibility()
        self.assertEqual(t.getVisibility(), True, "Visibility wasn't changed to True correctly")


if __name__ == "__main__": 
    unittest.main()