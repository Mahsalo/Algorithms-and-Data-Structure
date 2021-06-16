#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 17:00:27 2021

@author: mahsa
"""
import numpy as np
def zeroMatrix(x):
    
    rows = []
    cols = []
    m,n = x.shape
    Y = np.zeros((m,n))
    for i in range(m):
        for j in range(n):
            if x[i,j]==0:
                rows.append(i)
                cols.append(j)
            else:
                Y[i,j]=x[i,j]
    Y[rows,:]=0
    Y[:,cols]=0
            
                
    return Y            
    
    
    
    
    
x = np.array([[0,2,3,22],[4,5,6,10],[7,8,0,9]])   
print("x is:\n",x)
print("The result is:\n",zeroMatrix(x))    