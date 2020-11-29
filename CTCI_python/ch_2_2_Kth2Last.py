#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 09:59:57 2020

@author: mahsa: We would like to use two pointers to catch kth to the last 
elements of the linked list
"""

class Node:
    def __init__ (self, val = None, n = None):
        self.data = val
        self.next = n        
class LinkedList:
    def __init__(self,h=None):
        self.head = h
    def printList(self):
        this_node = self.head
        while(this_node is not None):
            print(this_node.data)
            this_node = this_node.next
            
         

def Kth2Last(LL,k,n):
    ptr1 = LL.head
    ptr2 = LL.head
    newLL = LinkedList()
    for i in range(k-1):
        ptr1 = ptr1.next
   
    while ptr1 is not None:
        if ptr2 is not None:
            ptr2 = ptr2.next
            ptr1 = ptr1.next
        if ptr1.next == None:
            for i in range(k):
                if (ptr2==None):
                    return -1
                else:  
                    print(ptr2.data)
                    ptr2 = ptr2.next

LL = LinkedList()
e1 = Node(2)
e2 = Node(4)
e3 = Node(10)
e4 = Node(112)
e5 = Node(60)
e6 = Node(18)
e7 = Node(5)
LL.head = e1
e1.next = e2
e2.next = e3
e3.next = e4
e4.next = e5
e5.next = e6
e6.next = e7
#LL.printList()
k=3
n=7
Kth2Last(LL,k,n)        
