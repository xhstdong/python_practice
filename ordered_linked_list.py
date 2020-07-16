# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 11:34:09 2020

@author: stdon
"""

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
        
class OrderedList:
    
    def __init__(self):
        #the head points to the location of the first node
        self.head=None
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
        return 'OrderedList'+str(item_list)
        
    def isEmpty(self):
        return self.head == None
    
    #we add nodes right at head for convenience
    def add(self, val):
        new_node = Node(val)
        
        prev_node = None
        current_node = self.head
        
        while current_node !=None and current_node.getData() < val:
            prev_node = current_node
            current_node = current_node.getNext()
        
        new_node.setNext(current_node)
        if prev_node == None:
            self.head = new_node
        else:
            prev_node.setNext(new_node)

        self.length += 1
        
    def size(self):
        # current_node=self.head
        # count = 0
        
        # while current_node != None:
        #     count += 1
        #     current_node = current_node.getNext() #go to next
        
        # return count
        return self.length
    
    
    def search(self, search_val):
        current_node=self.head
        found= False
        stop = False
        
        while current_node != None and not found and not stop:
            cur_val = current_node.getData() 
            if cur_val == search_val:
                found = True
            elif cur_val > search_val: #we assume list is increasing in value
                stop = True
            else:
                current_node = current_node.getNext()
        return found
    
    def remove(self, val):
        prev_node=None
        current_node = self.head
        
        #find the position of the value
        while current_node.getData() != val:
            if current_node.getData() > val: #we assume list is increasing in value
                print('the value is not found')
                return
            prev_node = current_node
            current_node = current_node.getNext()
            if current_node == None:
                print('the value is not found')
                return
        
        #change references to the current_node
        while (current_node != None) and (current_node.getData() == val):
            current_node=current_node.getNext()
            if prev_node == None:
            #then we have removed head, update head
                self.head = current_node
            else:
                prev_node.setNext(current_node)
            
            self.length -= 1
        # if temp_node ==None:
        #     #then we have removed the tail node, update tail
        #     self.tail = prev_node
        #del current_node
            
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
        
    # def append(self, val):
    #     new_node = Node(val)
    #     if self.isEmpty() == True:
    #         self.head = new_node
    #     else:
    #         self.tail.setNext(new_node)
            
    #     self.tail = new_node
mylist = OrderedList()
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
