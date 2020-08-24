#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 16:38:29 2020

@author: mahsa
In this module we find the n_th Fibonacci number
"""
import numpy as np

n=input()
n=int(n)
X=np.zeros((n+1,1))

##method 1, array implementation, not good for big inputs 
if n>0:
    X[1]=1
if n>1:
    for i in range(2,n+1):
        X[i]=X[i-1]+X[i-2]
print(int(X[n]))       

##method 2, without overflow
def fibonacciModulo(n): 
            
    previous, current = 0, 1
    if n==0: 
        return 0
    elif n==1: 
        return 1
    for i in range(n-1): 
        previous, current = current, previous + current 
          
    return (current) 

    