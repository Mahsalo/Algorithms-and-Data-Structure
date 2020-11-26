#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 11:15:10 2020

@author: mahsa: We would like to return the Kth to the last elements of a singly linked list
"""
import numpy as np

class Node:
    def __init__(self, data = None, n= None):
        self.val = data
        self.next = n
        
class LinkedList:
    def __init__(self, h = None): 
        self.head = h
        
    def printList(self):
        this_node = self.head
        while (this_node is not None):
            print(this_node.val)
            this_node = this_node.next

    def getSize(self):
        this_node = self.head
        cnt = 0
        while(this_node is not None):
            cnt +=1
            this_node= this_node.next 
        return cnt    

def IsPalindrome(listNode):
     this_node = listNode.head
     stack1 = []
     stack2 = []
     stack_tmp = []
     l = listNode.getSize()
     for i in range(l):
         x = this_node.val
         this_node = this_node.next
         if i < np.floor(l/2):
             stack1.append(x)
         if l%2 ==0:    
             if i>=np.floor(l/2):
                 stack2.append(x)
         else:
             if i>np.floor(l/2):
                 stack2.append(x)
     for j in range (len(stack2)):
         stack_tmp.append(stack2[-1])
         stack2.pop()
     if l == 1:
         return True
     print('stack1',stack1)
     print('stack2',stack_tmp)
     if stack1 == stack_tmp:
         return True
     else:
         return False
         
    
myList = LinkedList()
e1 = Node(11)
myList.head = e1
e2 = Node(1)
e3 = Node(22)
e4 = Node(100)
e5 = Node(10)
e6 = Node(3)
e7 = Node(5)
e8 = Node(18)    
e9 = Node(200)
e10 = Node(7)    
e1.next = e2
e2.next = e3
e3.next = e4 
e4.next = e5
e5.next = e6
e6.next = e7 
e7.next = e8
e8.next = e9
e9.next = e10 
myList.printList()
myList2 = LinkedList()
f1 = Node('a')
myList2.head = f1
f2 = Node('b')
f3 = Node('c')
f4 = Node('b')
f5 = Node('a')
f1.next = f2
f2.next = f3
f3.next = f4
f4.next = f5
print(myList.getSize())
print(IsPalindrome(myList))
myList2.printList()
print(IsPalindrome(myList2))
        