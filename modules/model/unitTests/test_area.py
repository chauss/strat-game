'''
Created on 30.03.2014

@author: Chris
'''
import unittest
from modules.model.area import Area

class AreaTest(unittest.TestCase):
    def testCreateArea(self):
        sa = Area()
        sa.addFieldCoords(0, 0)
        self.assertTrue(sa.isFieldInArea(0, 0), "Field (0/0) is not in area after adding it")
        self.assertFalse(sa.isFieldInArea(2, 2))
        sa.delFieldCoords(0, 0)
        self.assertFalse(sa.isFieldInArea(0, 0))
        