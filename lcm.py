#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 18:08:11 2020

@author: mahsa

In this module we find the Least Common Multiple of tw integers. 
There are 3 ways to do so:
    1) Iterate through all multiples of each number and detect the smallest common one
    2) Find the common prime factors and try to include them all in one number
    3) lcm(a,b)=a*b/gcd(a,b)
We implemented the easiest one, the third one.
  
"""

import numpy as np

def Mygcd(a,b):
    A=max(a,b)
    B=min(a,b)
    r=1
    while r>0:
        r=np.mod(A,B)
        if r!=0:
            A=B
            B=r
        else:
            q=B
    return(q)        

X=input()
X_mod=X.split()
a=int(X_mod[0])
b=int(X_mod[1])
GCD_ab=Mygcd(a,b)
LCM_ab=a*b/GCD_ab
print(int(LCM_ab))