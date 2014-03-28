'''
Created on 27.03.2014

@author: Chris
'''

class InvalidRankError(Exception):
    def __init__(self, invalidRank):
        self.invalidRank = invalidRank
        
    def __str__(self):
        from model import token
        return "Rank %d is not within %d and %d" % (self.invalidRank, token.MIN_RANK, token.MAX_RANK)
    
class IllegalMoveError(Exception):
    def __init__(self, field):
        self.occupiedField = field
        
    def __str__(self):
        return "Field is occupied: field_id=%s" % self.occupiedField