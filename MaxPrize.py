#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 18:45:20 2020

@author: mahsa
In this module we try to find th4e best pattern of summation of K 
integers that would sum up to fixed value "n".
"""

import numpy as np


n=int(input())
d=[]
k=n
l=1
factor=True
while factor:
    if k<=2*l:
        d.append(k)
        
        factor=False
    else:
        d.append(l)
        k=k-l
        l=l+1
print(len(d))       
print(*d, sep = " ")        


    




