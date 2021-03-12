#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 18:26:58 2021

@author: mahsa
In this module, we have implemented the code that represents incrementing an integer in an array
"""

def Increment(x):
    carry = 0
    l = len(x)
    result = [0]*l
    for i in reversed(range(l)):
        if i == l-1:
            x[i] = x[i]+1 
            
        summ = x[i]+carry 
        carry = 0
        if summ >=10:
            carry +=1
            result [i] = summ % 10
        else:
            result[i] = summ 
        summ = 0 
        if i == 0 and carry !=0 :
            extra = [carry]
            print(extra)
        else: 
            extra = []
    return extra+result        
            

x = [9,9,9]
y = [2,5,9]
print(Increment(x))    
print(Increment(y))    
