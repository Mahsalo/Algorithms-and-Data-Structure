#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 11:50:04 2020

@author: mahsa
In this module, we find the optimal solution of the coin change problem using
Greedy Algorithm, with a set of 1,5,10 cents we would like to choose a pattern
with the minimum number of coins that sum up to "m" which is given as an input
"""

# Uses python3
import sys
import numpy as np


def get_change(m):
    s=np.sort([1,5,10])
    s=s[::-1]
    summ=1
    i=0
    j=0

    while summ!=0:
        summ=int(m)-int(s[i])
        if summ<0:
            i+=1
        else:
            j+=1
            m=summ
       
    return j

m=input()
print(get_change(m))
