#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 09:01:10 2020

@author: mahsa
In this module we find the last digit of the sum of Fibonacci numbers
"""

import numpy as np

n=input()
n=int(n)
newN=np.mod(n,60)
F=np.zeros((newN+1))
if newN>0:
    F[1]=1
if newN>1:
    for i in range(2,newN+1):
        F[i]=np.mod(F[i-1],10)+np.mod(F[i-2],10)
        
s=np.sum(F)%10
print(int(s))        
