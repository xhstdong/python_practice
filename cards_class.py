# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 16:43:33 2020

@author: stdon
"""

class Card:
    
    def __init__(self, val, suit):
        self.val = val
        self.suit = suit
        
    def __repr__(self):
        return "%r (val=%r, suit=%r)" % (self.__class__.__name__, self.val, self.den)

    #def get_val(self):
    #    return self.val
    
    #def get_suit(self):
    #    return self.suit
    
    def set_val(self, val):
        self.val = val
    
    def set_suit(self, suit):
        self.suit = suit
        

card1=Card(10, 'hearts')