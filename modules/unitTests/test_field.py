'''
Created on 27.03.2014

@author: Chris
'''

import unittest
import field
import token
import player
from modules.myExceptions import IllegalMoveError

class FieldTest(unittest.TestCase):
    def testCreateField(self):
        f = field.Field()
        self.assertEqual(f.isOccupied(), None, "Field is occupied after initialization")
        
    def testChangeOccupiedStatus(self):
        p = player.Player("TestPlayer")
        f = field.Field()
        t = token.Token(1, p)
        f.moveTo(t)
        self.assertEqual(f.isOccupied(), t, "The token on the field is not the one who entered it")
        self.assertRaises(IllegalMoveError, f.moveTo, t)
        f.leave()
        self.assertEqual(f.isOccupied(), None, "The field is not empty/None after leaving it")
      
if __name__ == "__main__": 
    unittest.main()  