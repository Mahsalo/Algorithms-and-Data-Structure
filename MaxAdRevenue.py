#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 12:27:31 2020

@author: mahsa
In this module, we find the best permutations of two vectors such that the inner
product is maximized, It is called maximum Ad revenue such that the biggest Ad slot
is allocated to the most profitable Ad.
inputs:
    -number of Ads
    -Profit per Ad: a
    -Slot size: b
output:
    -Maximum a.b    
"""

import numpy as np


n=input()
n=int(n)

a=input()
a=a.split()
a=np.array(a).astype(int)

b=input()
b=b.split()
b=np.array(b).astype(int)

a_s=np.sort(a)
a_s=a_s[::-1]

b_s=np.sort(b)
b_s=b_s[::-1]

maxRev=np.multiply(a_s,b_s)
print(np.sum(maxRev).astype(int))



