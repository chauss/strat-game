'''
Created on 27.03.2014

@author: Chris
'''

class InvalidRankError(Exception):
    def __init__(self, invalidRank):
        self.invalidRank = invalidRank
        
    def __str__(self):
        import Token
        return "Rank %d is not within %d and %d" % (self.invalidRank, Token.MIN_RANK, Token.MAX_RANK)