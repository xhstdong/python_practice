# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 14:34:41 2020

@author: stdon
"""

def gcd(m,n):
    while m%n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm%oldn
    return n

class Fraction:
     def __init__(self,top,bottom):
         assert all (isinstance(i, int) for i in [top, bottom]), 'input must be integers'
         common = gcd(top, bottom)
         self.num = top//common
         self.den = bottom//common

     def __str__(self):
         return str(self.num)+"/"+str(self.den)

     def __repr__(self):
         #return f'{self.__class__.__name__}(num={self.num!r}, den={self.den!r})'
         return "%r (num=%r, den=%r)" % (self.__class__.__name__, self.num, self.den)
     
     def show(self):
         print(self.num,"/",self.den)
         
     def get_num(self):
         return self.num
     
     def get_den(self):
         return self.den

     def __add__(self,otherfraction):
         newnum = self.num*otherfraction.den + \
                      self.den*otherfraction.num
         newden = self.den * otherfraction.den
         common = gcd(newnum,newden)
         return Fraction(newnum//common,newden//common)
     
     def __radd__(self, otherfraction):
         return self.__add__(otherfraction)

     def __iadd__(self, otherfraction):
         newnum = self.num*otherfraction.den + \
                      self.den*otherfraction.num
         newden = self.den * otherfraction.den
         common = gcd(newnum,newden)
         self.num = newnum//common
         self.den = newden//common
         return self

     def __eq__(self, other):
         firstnum = self.num * other.den
         secondnum = other.num * self.den
         return firstnum == secondnum

x = Fraction(1,2)
print(x)
y = Fraction(2,-3)
print(x+y)
print(x == y)
x += y
print(x)
