#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 17:27:27 2020

@author: mahsa
In this module, we try to find the best combination of items that 
the sum of the value would be maximum (Knapsack problem).
The input: First Line: maximum number of items allowed and the full capacity
The next lines show the weight and the value of the items
The output: The maximum value put in the bag
The solution would be to sort in terms of value-per-weight

"""

import numpy as np

def maxVal(n,capacity,V,W):
    V_per_W=[]
    for j in range (len(V)):
        V_per_W.append(float(V[j]/W[j]))
    sorted_units=np.sort(V_per_W)
    sorted_ind=np.argsort(V_per_W)
    s=sorted_ind[::-1]#Ascending indices
    newW=W[s]
    newV=V[s]
    factor=True
    i=0
    sumVal=0
    c=capacity

    while factor and i<n:

        if c>=newW[i]:#put the whole item in the bag
            c=c-newW[i]
            sumVal=newV[i]+sumVal
            i+=1
        else:#just put a fraction of the item in the bag
            sumVal+=(c/newW[i])*newV[i]
            factor=False
    return sumVal        
            
first_line=input()
X=first_line.split()
n=int(X[0])
capacity=int(X[1])
V=np.zeros((n,1))
W=np.zeros((n,1))

for i in range (0,n):
    lines=input()
    lines=lines.split()
    V[i]=int(lines[0])
    W[i]=int(lines[1])
print("%.4f" % maxVal(n,capacity,V,W))    
