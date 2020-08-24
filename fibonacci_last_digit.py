#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 16:38:29 2020

@author: mahsa
In this module we find the last digit of the n_th Fibonacci number. 
In finding the next number we can only use the last digits of the
last two numbers to avoid overflow.
"""
import numpy as np

n=input()
n=int(n)
X=np.zeros((n+1,1))
if n>0:
    X[1]=1

if n>1:
    for i in range(2,n+1):
        X[i]=np.mod(X[i-1],10)+np.mod(X[i-2],10)
print(int(X[n]%10))  
 
    