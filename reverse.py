# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 10:38:00 2020

@author: stdon
"""

from test import testEqual
def reverse(s):
    if len(s) == 0:
        return s
    else:
        return s[-1] + reverse(s[:-1])

testEqual(reverse("hello"),"olleh")
testEqual(reverse("l"),"l")
testEqual(reverse("follow"),"wollof")
testEqual(reverse(""),"")