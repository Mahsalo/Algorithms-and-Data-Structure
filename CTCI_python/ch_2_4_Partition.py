#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 19:53:19 2020

@author: mahsa
"""
class Node:
    def __init__(self,val = None, n = None):
        self.next = n
        self.data = val
        
class LinkedList:
    def __init__(self,h=None):
        self.head =  h
        
    def printList(self):
        this_node = self.head
        while(this_node is not None):
            print(this_node.data)
            this_node = this_node.next

def partition(head, x):
        this_node = head
        right = []
        left = []
        while this_node is not None:
            
            if this_node.data < x:
                left.append(this_node.data)

            if this_node.data >=x:
                right.append(this_node.data)
 
            this_node = this_node.next  
        merged = left+right
        
        ResLL = LinkedList()
        X  = Node(merged[0])
        ResLL.head = X
        
        for i in range(1,len(merged)):
            Y =  Node(merged[i])
            X.next= Y 
            X = X.next
                
        #ResLL.printList()  
        return ResLL
        
LL = LinkedList()
e1 = Node(1)
e2  = Node(3)  
e3  = Node(2)  
e4  =Node(5)  
e5  = Node(2)  
x=3
LL.head = e1
e1.next =  e2
e2.next = e3
e3.next = e4
e4.next = e5
#LL.printList()
partition(LL.head,x).printList()

