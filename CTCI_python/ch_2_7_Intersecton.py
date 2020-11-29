#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 11:44:46 2020

@author: mahsa
"""

class Node:
   def __init__(self, data=None, next = None):
      self.data = data
      self.next = next
class LinkedList:
    def __init__(self,h=None):
        self.head = h
    def printLL(self):
        this_node = self.head
        while this_node is not None:
            print(this_node.data)
            this_node=this_node.next
        
        

def getIntersectionNode(headA,headB):
        d = {}
        while headA is not None:
            d[headA] = 1
            headA = headA.next
        while headB is not None:
            if headB in d:
                return headB.data
            headB = headB.next
        return None    
     
LL1 = LinkedList()
LL2 = LinkedList()

e1 = Node(2)
e2 = Node(4)
e3 = Node(8)
e4 = Node(15)
e5 = Node(22)

e6 = Node(23)
e7 = Node(12)

LL1.head = e1
e1.next = e2
e2.next = e3
e3.next = e4
e4.next = e5

LL2.head = e6
e6.next = e7
e7.next = e4

print(getIntersectionNode(LL1.head,LL2.head))

  