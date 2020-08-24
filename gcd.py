#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 17:34:31 2020

@author: mahsa
In this module we find the Greatest Common Divisor of two integers using Euclidean
Algorithm. Find the remainder and replace the reaminder with the quotient until 
you hit 0 in the remainder.  
"""
import numpy as np
import sys

X=input()
Y=X.split()
a=int(Y[0])
b=int(Y[1])

A=max(np.abs(a),np.abs(b))
B=min(np.abs(a),np.abs(b))
r=1;
while r>0:
    r=np.mod(A,B)
    if r!=0:
        A=B
        B=r
    else:
        q=B
print(q)        
        
