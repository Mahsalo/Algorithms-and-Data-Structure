#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 20:16:27 2021

@author: mahsa
"""

class setOfStacks:
    def __init__(self,n):
        self.stack = []
        self.capacity = n
        self.num=0
        self.stackNum =0
        self.extra = []
        
    
    def push(self,x):

        if self.num>=self.capacity:
            
            self.stack.append([x])
            self.stackNum +=1
            self.num = 0
        else:
            if len(self.stack)==0:
                self.stack.append([x])   
            else:
                self.stack[self.stackNum].append(x) 
          
        self.num +=1    
        print('result of push:',self.stack)
        return None
        
    
    def pop(self):
        temp= self.stack[self.stackNum][-1]
        self.stack[self.stackNum].pop()
        if len(self.stack[self.stackNum])==0:
            self.stack.pop()
            self.stackNum -=1
            self.num =self.capacity
        else:
            self.num -=1
   
        print('result of pop:',self.stack)
        return None
    
    
    def popAt(self,ind):
        r=int(ind % self.capacity)
        q=int(ind / self.capacity)
        
        for i in range(len(self.stack[q])):
            
            self.extra.append(self.stack[q][-1])
            self.stack[q].pop()
        self.extra.pop()    
        
        if len(self.stack[q])==0:
            self.stack[q]=[j for j in self.extra][::-1]
        else:
            self.stack[q]=self.stack[q]+ self.extra.reverse()   
        print('result of pop at is:',self.stack)
        return None
    
    
obj = setOfStacks(3)
obj.push(12)
obj.push(10) 
obj.push(13)
obj.push(14)  
obj.push(15) 
obj.push(22)
obj.push(0)
obj.pop()
obj.push(111)
obj.push(100)
obj.pop()
obj.push(1111)
obj.popAt(4)
