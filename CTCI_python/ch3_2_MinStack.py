#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 15:48:43 2020

@author: mahsa
"""



class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """      
        self.stack = []
        self.MinStack= []
        
    def push(self, x: int) -> None:
        self.stack.append(x)
        if len(self.MinStack)==0:
            self.MinStack.append(x)
        else:
            if x<=self.MinStack[-1]:
                self.MinStack.append(x)      
        return None
    def pop(self) -> None:
        
        if len(self.MinStack)!=0:
            if self.stack[-1]==self.MinStack[-1]:
                self.MinStack.pop()
                self.stack.pop()
            else:
                self.stack.pop()
                
        return None

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.MinStack[-1]
        


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(1)
obj.push(-2)
obj.push(34)
obj.push(2)
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()