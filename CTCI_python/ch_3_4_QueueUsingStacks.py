#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 10:22:06 2021

@author: mahsa

We should either make enqueue costly or make dequeue costly (one of them)
I have made dequeue (pop) costly (O(N)) but the push operation takes O(1) time 
"""

class QueueWStack:
    def __init__(self):
        self.s1 = []
        self.s2 = []
        
    def push(self,x):
        self.s1.append(x)
        print('The result of the push operation',self.s1)
        
    def pop(self):
        n = len(self.s1)
        if len(self.s1)==0:
            print('Nothing to pop')
            return None
        for i in range(len(self.s1)-1):
            self.s2.append(self.s1[-1])
            self.s1.pop()
        print(self.s2)   
        if i == n-2:
            print('Item to pop is:',self.s1[0])
            self.s1.pop()
            for j in range(len(self.s2)):
                self.s1.append(self.s2[-1])
                self.s2.pop()
                
        print('the result after poping is:',self.s1)

obj=QueueWStack()
obj.push(11)
obj.push(13)
obj.push(22)
obj.push(28)
obj.pop()
obj.push(123)
obj.pop()




             
            