# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 10:08:13 2020

@author: stdon
"""
import unordered_linked_list

class Stack:
     def __init__(self):
         self.items = UnorderedList()

     def isEmpty(self):
         return self.items.isempty() == True

     def push(self, item):
         self.items.add(item)

     def pop(self):
         return self.items.remove(self.items.head.getData())

     def peek(self):
         return self.items.head.getData()

     def size(self):
         return self.items.size()
