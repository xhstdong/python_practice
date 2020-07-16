# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 10:26:23 2020

convert a number to string using a different base (not 10)
@author: stdon
"""

def toStr(n,base):
   convertString = "0123456789ABCDEF"
   if n < base:
      return convertString[n]
   else:
      return toStr(n//base,base) + convertString[n%base]

print(toStr(1453,16))
