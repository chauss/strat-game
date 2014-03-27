'''
Created on 27.03.2014

@author: Chris
'''

import unittest
import Field
import Token
from Exceptions import IllegalMoveError

class FieldTest(unittest.TestCase):
    
    def testCreateField(self):
        f = Field.Field()
        self.assertEqual(f.isOccupied(), None, "Field is occupied after initialization")
        
    def testChangeOccupiedStatus(self):
        f = Field.Field()
        t = Token.Token(1)
        f.moveTo(t)
        self.assertEqual(f.isOccupied(), t, "The token on the field is not the one who entered it")
        self.assertRaises(IllegalMoveError, f.moveTo, t)
        f.leave()
        self.assertEqual(f.isOccupied(), None, "The field is not empty/None after leaving it")
        