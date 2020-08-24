#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 09:32:26 2020

@author: mahsa

In this module we find the last digit of the sum of the Fibonacci numbers in a range [m,n]
If the input numbers are not that big, we can use the array implementation of the Fibonacci numbers

"""

import numpy as np

def Fib(x):
    F=np.zeros((x+1,1))
    if x>0:
        F[0]=0
    if x>1:
        F[1]=1
        for i in range(2,x+1):
            F[i]=F[i-1]+F[i-2]
    return F[x]       

X=input()
X=X.split()
N=int(X[0])
M=int(X[1])
n=max(M,N)
m=min(M,N)

s=Fib(n+2)-Fib(m+1)
if m==n:
    s=Fib(n)
print(int(s%10))




