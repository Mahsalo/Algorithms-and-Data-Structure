#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 14:29:35 2021

@author: mahsa
In this module we will find the reverse of the binary sequence
"""
import numpy as np
import math

def reverseBits(X):
    a = bin(X)
    a = a.replace("0b","")
    a = a[::-1]
    return int(a)
    

def CoolReverse1(X): ### O(N)
    a = bin(X)
    a = a.replace("0b","")
    l = len(a)
    position = l-1
    summ = 0
    while X !=0:
       Y=(X&1)<<position 
       summ = summ | Y
       position -=1
       X = X>>1
      
    return summ 

def CoolReverse2(X): ### O(N)
    a = bin(X)
    a = a.replace("0b","")
    l = len(a)
    p= l-1
    Y= np.zeros((l,1))
    for i in range (math.floor(l/2)):
        x1 = a[i]
        x2 = a[p]
        Y[i] = x2
        Y[p] = x1
        p-=1
        
    return Y    
  
print(reverseBits(18))    
print(CoolReverse1(18))    
print(CoolReverse2(18))    
  
