#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 15:58:45 2020

@author: mahsa: We would like to delete any given node by only having access to that specific node
We don't have access to the head of the linked list
"""

class Node:
    def __init__ (self, val = None, n = None):
        self.data = val
        self.next = n
        
class LinkedList:
    def __init__(self, h=None):
        self.head = h
        self.size = 0
    def printList(self):
        this_node = self.head
        while(this_node is not None):
            print(this_node.data)
            this_node =  this_node.next
    def RemoveByIndex(self,MidNode):###remove the k_th element of the linked list
         
         if MidNode is None or  MidNode.next is None:
             return False
         E = MidNode.next
         MidNode.data = E.data
         MidNode.next = E.next
         return True

     
    





       
            
    
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
print("The linked list before the removal of the mid point\n")
myList.printList()
MidNode = e3
myList.RemoveByIndex(e3)##deleting 10
print("The linked list after the removal of the mid point\n")

myList.printList()
        
        
        
        
                   
        
        