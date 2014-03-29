'''
Created on 28.03.2014

@author: Chris
'''
import unittest

from .. import player


class PlayerTest(unittest.TestCase):
    
    def testCreatePlayer(self):
        p = player.Player("TestPlayer", 1)
        self.assertEqual(p.getName(), "TestPlayer", "Name of Player wasn't initialized correct")
        
    def testGetIndex(self):
        p = player.Player("TestPlayer", 1)
        self.assertEqual(p.getIndex(), 1, "The index of the player wasn't initialized correct")
