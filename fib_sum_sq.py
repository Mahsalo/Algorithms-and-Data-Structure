#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 09:50:38 2020

@author: mahsa
In this module we find the sum of the squares of the Fibonacci numbers.
The easiest way to find the sum of Squares of the first n Fibonacci numbers is
to find F(n+1)*F(n) (The area of a rectangle formed by Fibonacci numbers)
"""

import numpy as np

def Fib(n):
    current=0
    if n==0:
        current=0
    if n==1:
        pre1=0
        current=1
    if n>1:
        pre1=0
        pre2=1
        n=n%60
        for i in range(n-1):
            current=pre1+pre2  
            pre1=pre2
            pre2=current
    return current        


X=input()
X=int(X)
h=Fib(X+1)
v=Fib(X)
sum_sq=(h)*(v)
print(sum_sq%10)


