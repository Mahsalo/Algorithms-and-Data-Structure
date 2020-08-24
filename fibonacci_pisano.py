#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 20:25:03 2020

@author: mahsa

In this module, we find the (Fn mod m), the remainder of a Fibonacci number divided 
by an integer m. n could be really big so it's better not to use the array-implementation 
of Fibonacci numbers. We make use of Pisano Period length since (Fn mod m)
iterates after Pisano period length of m.
F2015 mod 3= F7 mod 3=1 
Since 2015 mod 8=7 and 8 is the Pisano Period of 3.

"""
import numpy as np
def pisanoPeriod(m):
    d0=0
    d1=1
    for i in range (0,m*m):
        d=(d0+d1)%m
        d0=d1
        d1=d
        if d0==0 and d1==1:
            return (i+1)
##method 1        
def Fib(n):        
    F=np.zeros((n+1,1))
    if n>0:
        F[1]=1
    if n>1:
        for i in range(2,n+1):
            F[i]=F[i-1]+F[i-2]
    return F[n] 
##method 2, without overflow, faster
def fibonacciModulo(n): 
            
    previous, current = 0, 1
    if n==0: 
        return 0
    elif n==1: 
        return 1
    for i in range(n-1): 
        previous, current = current, previous + current 
          
    return (current) 

X=input()
X_mod=X.split()
F=int(X_mod[0])
m=int(X_mod[1])
p=pisanoPeriod(m)   
new_F=F%p
r=float(Fib(new_F))%m
r2=fibonacciModulo(new_F)%m
print(r2)

       