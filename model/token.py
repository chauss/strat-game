'''
Created on 26.03.2014

@author: Chris
'''
import logging
log = logging.getLogger("token_logger")
format = logging.Formatter("%(asctime)s [%(levelname)-8s] - %(name)s: %(message)s", 
                              "%d.%m.%Y %H:%M:%S")
handler = logging.FileHandler

class Token():
    def __init__(self, rank):
        self.__rank = rank

    def setRank(self, newRank):
        self.__rank = newRank
        
    def getRank(self):
        return self.__rank