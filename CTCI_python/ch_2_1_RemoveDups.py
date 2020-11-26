#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 15:58:45 2020

@author: mahsa: We would like to delete the duplicates from an unsorted linked list
"""

class Node:
    def __init__(self,val=None,n=None):
        self.data = val
        self.next = n
        
    def get_next(self):
        return self.next
    
    def set_next(self,x):
        self.next = x
        
    def get_data(self):
        return self.data
    
    def set_data(self,x):
        self.data = x

class LinkedList:
    def __init__(self,h=None):
        self.head = h
        self.size = 0
        
    def get_size(self):
        return self.size 
    
    def add(self,data):
        newNode = Node(data,self.head)
        self.head = newNode
        self.size +=1
    
    def remove(self,data):  
        this_node = self.head
        prev_node = None
        while(this_node):
           if this_node.get_data() == data:
              if prev_node:
                  prev_node.set_next(this_node.get_next()) 
              else:
                  self.head= this_node.next
              self.size -=1    
              return True
           else:       
              prev_node = this_node
              this_node = this_node.get_next()
           return False    
               
    def find(self,data):
        this_node = self.head
        while(this_node):
            if this_node.get_data() == data:
                return True
            else:
                this_node = this_node.get_next()
            return False
        
    def printList(self):
        this_node = self.head
        while(this_node is not None):
            print(this_node.data)
            this_node = this_node.next
     
def RemoveDups(listNode):     
    this_node = listNode.head
    hashT = [0]*256
    newLinkedList = LinkedList() #store the non-repeated values from the linked list
    i = 0
    while (this_node is not None):
        value = this_node.data
        print("val",value)
        if i ==0: #at first
            hashT[value] +=1
            e = Node(value)
            newLinkedList.head = e
        else:
            if hashT[value] == 0:
                e_next = Node(value)
                e.next = e_next
                hashT[value] +=1
                e = e.next
        
        this_node =this_node.next        
        i+=1 
    return newLinkedList        
            
    
    
    
    
myList = LinkedList()
e1 = Node(1)
e2 = Node(2)
e3 = Node(10)
e4 = Node(20)
e5 = Node(1)
e6 = Node(2)
e7 = Node(47)
e8 = Node(10)
myList.head = e1
e1.next = e2
e2.next = e3
e3.next = e4
e4.next = e5
e5.next = e6
e6.next = e7
e7.next = e8

myList.printList()
res = RemoveDups(myList)
res.printList()
        
        
        
        
                   
        
        