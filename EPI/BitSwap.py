#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 11:48:48 2021

@author: mahsa
In this module, we will swap the bits at (i,j) locations starting at location 0
"""

def BitSwap(X,i,j):
    X1 = X & (1<<i)
    X2 = X & (1<<j)
    
    if X2==0:
        bit_j =0
    else:
        bit_j=1
        X=X | (1<<i)
    if X1==0:
        bit_i=0
    else:
        bit_i=1
        X = X | (1<<j)
        
    if  bit_j ==0:
        X = X & ~(1<<i)   ## This term is used to unset the ith bit starting from bit 0 
    if  bit_i ==0:
        X = X & ~(1<<j)       
    print(bit_i,bit_j)    
    return X

X=45
loc1=1
loc2=3
A=BitSwap(X,loc1,loc2)
print("After swapping the {a}th and {b}th bits of {c}, it would become {d}".format(a=loc1,b=loc2,c=X,d=A))    
    