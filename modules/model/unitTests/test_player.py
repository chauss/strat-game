'''
Created on 28.03.2014

@author: Chris
'''
import unittest

import model.player as player


class PlayerTest(unittest.TestCase):
    
    def testCreatePlayer(self):
        p = player.Player("TestPlayer")
        self.assertEqual(p.getName(), "TestPlayer", "Name of Player wasn't initialized correct")
