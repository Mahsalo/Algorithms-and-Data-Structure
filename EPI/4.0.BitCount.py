#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 10:39:04 2021

@author: mahsa
In this module we try to count the number of bits=1 in an integer
"""

def count_bit(x):
    cnt = 0
    while x!=0:
        tmp = x&1
        if tmp ==1:
            cnt+=1
        x=x>>1
    return cnt    

X=15
r = count_bit(X)            
print('The count of th eONE bits in {a} is {b}'.format(a= X,b= r))        
