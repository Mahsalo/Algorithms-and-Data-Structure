#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 21:12:50 2020

@author: mahsa
We would like to find the  sum of  two numbers stored reverse in two linked lists 
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
    
    def getSize(self):
        this_node = self.head
        cnt=0 
        while(this_node is not None):
            cnt +=1
            this_node = this_node.next
        return cnt
    
def summation(A,B):
    carry = 0
    l_a = A.getSize()
    l_b = B.getSize()
    Res = LinkedList()
    
    i = 1

    if l_a >= l_b:
        maxVal = l_a
        minVal = l_b
    else:
        maxVal = l_b
        minVal = l_a
        
    this_node_a = A.head
    this_node_b = B.head  
             
    while i <= maxVal: 
        if  this_node_b is None:
            summ = this_node_a.data + carry
        elif this_node_a is None:
            summ = this_node_b.data + carry
        else:
            summ = this_node_a.data+this_node_b.data+carry
        if summ >=10:
            carry += 1
            s = summ % 10
        else:
            carry = 0
            s = summ
        if  i == 1:
            e = Node(s)
            Res.head = e
        else:
            e.next= Node(s)
            e = e.next
        if this_node_a is None:
            this_node_b = this_node_b.next
        elif this_node_b is None:
            this_node_a = this_node_a.next
        else:
            this_node_b = this_node_b.next
            this_node_a = this_node_a.next
        i+=1
    
    Res.printList()
    return  Res      
        

                      

a = LinkedList()
e1 = Node(1)
e2 = Node(2)
e3 = Node(9)
b = LinkedList()
e4 = Node(8)
e5 = Node(4)
e6 = Node(2)
e7 = Node(3)

a.head = e1
e1.next = e2
e2.next = e3
b.head = e4
e4.next = e5
e5.next = e6
e6.next = e7

summation(a,b)



