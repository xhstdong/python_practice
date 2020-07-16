# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 15:54:53 2020

@author: stdon
"""

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

#    def enqueue(self, item):
#        self.items.insert(0,item)
    def enqueue(self, item):
        self.items.append(item)

    # def dequeue(self):
    #     return self.items.pop()
    def dequeue(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)
    
myQue = Queue()
myQue.enqueue(5)
myQue.enqueue('random')
myQue.enqueue('10')
print(myQue.dequeue())
myQue.enqueue(3)
print(myQue.dequeue())