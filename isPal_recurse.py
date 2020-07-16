# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 10:38:03 2020

@author: stdon
"""

from test import testEqual
def removeWhite(s):
    alphabet='abcdefghijklmnopqrstuvwxyz'
    return ''.join(i for i in s if i in alphabet)

def isPal(s):
    if len(s) < 2:
        return True
    else:
        return s[0]==s[-1] and isPal(s[1:-1])

testEqual(isPal(removeWhite("x")),True)
testEqual(isPal(removeWhite("radar")),True)
testEqual(isPal(removeWhite("hello")),False)
testEqual(isPal(removeWhite("")),True)
testEqual(isPal(removeWhite("hannah")),True)
testEqual(isPal(removeWhite("madam i'm adam")),True)