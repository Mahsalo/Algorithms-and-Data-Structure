#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 08:32:39 2020

@author: mahsa

Insert binary rep. M into the binary rep. N, M and N are binary sequences
"""
import numpy as np

def Binary2Decimal(x): # x is a string of binary values
    s = 0
    if type(x) is not str:
        x_s = str(x) # we assume that the binary sequences don't have leading zeros
    else:
        x_s = x
    for i in range(len(x_s)):
        ind = len(x_s)-i-1
        s = s + 2**ind * int(x_s[i])
    return s  
  

def BitInsertion(x1,x2,i1,i2):##insert the smaller binary rep. into the bigger binary rep. in i1:i2, x1 and x2 are integers
    if i1<i2:
        tmp = i1
        i1= i2
        i2 = tmp
        
    right_mask = (1<<i2)-1
    left_mask = ~0 ##all ones
    left_mask = left_mask << (i1+1)
    ###left_mask = ~(1<<(i1+1)-1) Second solution
    range_mask = right_mask | left_mask
    
    x2_mod = x2<<i2
    x1_mod = x1 & range_mask
    result = x1_mod | x2_mod

    return bin(result)
        

x1 = 10000000000
x2 = 10011
x1_int = Binary2Decimal(x1)
x2_int = Binary2Decimal(x2)

i1 = 6
i2 = 2
print(BitInsertion(x1_int,x2_int,i1,i2))    
    
