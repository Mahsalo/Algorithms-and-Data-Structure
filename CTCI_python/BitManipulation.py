#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 07:31:44 2020

@author: mahsa
"""

def getBit(s,i):### S is an integer number and ith bit of the binary representation is desired
    mask = (1<<i)# The result would be an integer number but the one is moving in binary rep.
    AndVal = s & mask
    if AndVal != 0 :
        return 1
    else:
        return 0
i1 = 3
num1 = 9
r1 = getBit(num1,i1)
r2 = getBit(4,2)    
print('The bit number {i1} of binary rep. of {num1} is: {r1}'.format(i1=i1,r1=r1,num1=num1)) 

def setBit(s,i): ## Set the ith bit of integer num. s to 1
    mask = (1<<i)
    OrVal = s | mask
    return OrVal

i1 = 2
num1 = 9
r1 = setBit(num1,i1)  
print('By setting the bit number {i1}, {num1} becomes {r1}'.format(i1=i1,r1=r1,num1=num1)) 

def clearBit(s,i):### Set the ith bit of s to zero
    mask = ~(1<<i) # this mask has only one zero at ith bit, the rest of them are 1
    AndVal = s & mask
    return AndVal

i1 = 3
num1 = 9
r1 = clearBit(num1,i1)  
print('By clearing the bit number {i1}, {num1} becomes {r1}'.format(i1=i1,r1=r1,num1=num1)) 
    

def clearDown(s,i): ### (i inclusive) clear the bits from i to 1 in s, we need a mask like 11111000
    mask1 = (1<<i)
    mask2 = mask1 - 1 ## 00000100 - 1 = 00000011, i is 2 here
    mask3 = ~mask2 ##11111100
    AndVal = s & mask3
    return AndVal

i1 = 3
num1 = 15
r1 = clearDown(num1,i1)  
print('By clearing from the bit number {i1} to LSB, {num1} becomes {r1}'.format(i1=i1,r1=r1,num1=num1)) 

def clearUp(s,i):
    mask1 = (1<<i)
    mask2 = mask1 - 1
    AndVal = s & mask2
    return AndVal

i1 = 3
num1 = 15
r1 = clearUp(num1,i1)  
print('By clearing from the bit number {i1} to MSB, {num1} becomes {r1}'.format(i1=i1,r1=r1,num1=num1))    

