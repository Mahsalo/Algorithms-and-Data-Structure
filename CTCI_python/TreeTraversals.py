#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 14:39:35 2020

@author: mahsa
In this module, we have implemented a BST with minimal height
such that the root at each level is the middle point of the 
sub-array
"""

class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data
        
def PrintInOrder(root):## Root is an object
    if root:
        PrintInOrder(root.left)
        print(root.data)
        PrintInOrder(root.right)

def PrintPostOrder(root): 
    if root:
        PrintPostOrder(root.left)
        PrintPostOrder(root.right)
        print(root.data)

def PrintPreOrder(root):
    if root:
        print(root.data)
        PrintPreOrder(root.left)  
        PrintPreOrder(root.right)
        
obj = Node(2)
obj.left = Node(3)
obj.right = Node(10)
obj.left.left = Node(1)
obj.left.right = Node(11)
obj.right.left = Node(20)
obj.right.right = Node(19)
print('Inorder')
PrintInOrder(obj)
print('PostOrder')
PrintPostOrder(obj)
print('PreOrder')
PrintPreOrder(obj)





