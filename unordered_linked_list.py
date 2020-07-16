# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 17:13:33 2020

@author: stdon
"""

class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext
        
class UnorderedList:
    
    def __init__(self):
        #the head points to the location of the first node
        #the tail points to the location of the last node
        self.head=None
        self.tail=None
        self.length = 0
    
    def __str__(self):
        item_list = []
        current_node = self.head
        while current_node != None:
            item_list.append(current_node.getData())
            current_node = current_node.getNext()
        return str(item_list)
    
    def __repr__(self):
        item_list = []
        current_node = self.head
        while current_node != None:
            item_list.append(current_node.getData())
            current_node = current_node.getNext()
        return 'UnorderedList'+str(item_list)
    
    def slice(self, start, stop):
        item_list = []
        current_node = self.head
        count = 0
        while current_node < start:
            count += 1
            current_node = current_node.getNext()
        while current_node < stop:
            count += 1
            item_list.append(current_node.getData())
            current_node = current_node.getNext()
            
        return item_list
            
    
    def isEmpty(self):
        return self.head == None
    
    #we add nodes right at head for convenience
    def add(self, val):
        new_node = Node(val)
        new_node.setNext(self.head) #set the next node to the previous first node
        #update tail node
        if self.head == None:
            self.tail =new_node
            
        self.head = new_node #set new first node
        self.length += 1
        
    def size(self):
        return self.length
        # current_node=self.head
        # count = 0
        
        # while current_node != None:
        #     count += 1
        #     current_node = current_node.getNext() #go to next
        
        # return count
    
    
    def search(self, search_val):
        current_node=self.head
        found= False
        while current_node != None and not found:
            if current_node.getData() == search_val:
                found = True
            else:
                current_node = current_node.getNext()
        return found

#a more useful function than search    
    def index(self, search_val):
        current_node = self.head
        found = False
        count=0
        while curret_node != None and not found:
            if current_node.getData() == search_val:
                found = True
            else:
                count +=1
                current_node = current_node.getNext()
        if found == True:    
            return count
        else:
            return found
    
    def insert(self, pos, item):
        prev_node = None
        current_node = self.head
        count = 0
        new_node = Node(val)
        
        if pos == 0:
            self.add(item)
        elif pos == self.size():
            self.append(item)
        elif pos > self.size():
            print('Cannot execute command. List only has size {}'.format(self.size()))
        else:        
            while count < pos:
                count += 1
                prev_node = current_node
                current_node = current_node.getNext()
            
            prev_node.setNext(new_node)
            new_node.setNext(current_node)
            self.length += 1
                
            

 
    #this implementation assumes duplicates
    def remove(self, val):
        prev_node=None
        current_node = self.head
        
        #find the position of the value
        while current_node != None:

            
            if current_node.getData() == val:
                
                #change references to the current_node
                current_node=current_node.getNext()
                if prev_node == None:
                    #then we have removed head, update head
                    self.head = current_node
                else:
                    prev_node.setNext(current_node)
                if current_node ==None:
                    #then we have removed the tail node, update tail
                    self.tail = prev_node
                    
                self.length -= 1 

            else:
                prev_node = current_node
                current_node = current_node.getNext()
    
    #this implementation assumes no duplicates
    # def remove(self, val):
    #     prev_node=None
    #     current_node = self.head
        
    #     #find the position of the value
    #     while current_node.getData() != val:
    #         next_node = current_node.getNext()
    #         if next_node == None:
    #             print('the value is not found')
    #             return
    #         else:
    #             prev_node = current_node
    #             current_node = next_node
        
    #     #change references to the current_node
    #     temp_node=current_node.getNext()
    #     if prev_node == None:
    #         #then we have removed head, update head
    #         self.head = temp_node
    #     else:
    #         prev_node.setNext(temp_node)
    #     if temp_node ==None:
    #         #then we have removed the tail node, update tail
    #         self.tail = prev_node
            
    #     self.length -= 1
            
    #add a value at the very end
    # def append(self, val):
    #     new_node = Node(val)
    #     if self.isEmpty() == True:
    #         print('self is empty, set head to {}'.format(val))
    #         self.head = new_node
            
    #     else:
    #         current_node = self.head
    #         while current_node.getNext() != None:
    #             print('going to next node')
    #             current_node = current_node.getNext()
    #         print('reached the end')
    #         current_node.setNext(new_node)
    #     self.tail = new_node   
        
    def append(self, val):
        new_node = Node(val)
        if self.isEmpty() == True:
            self.head = new_node
        else:
            self.tail.setNext(new_node)
            
        self.tail = new_node
        self.length += 1
        
    def pop(self):
        prev_node = None
        current_node = self.head
        
        while current_node.getNext() != None:
            prev_node = current_node
            current_node = current_node.getNext()
    
        return_val = current_node.getData()
        prev_node.setNext(current_node.getNext())
        self.tail = prev_node
        self.length -= 1
        return return_val
        
mylist = UnorderedList()
mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)

print(mylist.size())
print(mylist.search(93))
print(mylist.search(100))
mylist.remove(93)
print(mylist.size())
mylist
print(mylist.pop())