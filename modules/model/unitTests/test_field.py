'''
Created on 27.03.2014

@author: Chris
'''

import unittest

from .. import field 
from ..myExceptions import IllegalMoveError
from .. import player
import my_token


class FieldTest(unittest.TestCase):
    def testCreateField(self):
        f = field.Field()
        self.assertEqual(f.getOccupyingToken(), None, "Field is occupied after initialization")
        
    def testChangeOccupiedStatus(self):
        p = player.Player("TestPlayer", 1)
        f = field.Field()
        t = my_token.Token(1, p)
        f.moveTo(t)
        self.assertEqual(f.getOccupyingToken(), t, "The my_token on the field is not the one who entered it")
        self.assertRaises(IllegalMoveError, f.moveTo, t)
        f.leave()
        self.assertEqual(f.getOccupyingToken(), None, "The field is not empty/None after leaving it")
      
if __name__ == "__main__": 
    unittest.main()  