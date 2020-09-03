#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 20:39:42 2020

@author: mahsa
In this module, we implement the binary search algoithm
in order to find k elements in an array, the output is the index 
of the elements in the array and -1 if there is none in the array
"""
import numpy as np

def BinSearch(low,high,A,key):
    mid=int(np.floor(low+(high-low)/2))
    if high>=low:
        if key==A[mid]:
            return mid
        else:
            if key>=A[mid]:
                new_low=mid+1
                return BinSearch(new_low,high,A,key)
            else:
                new_high=mid-1
                return BinSearch(low,new_high,A,key)
    else: 
        return -1
        

A=input()
A=A.split()


B=input()
B=B.split()
k=int(B[0])

l=len(A)
m=int(np.floor(l/2))
a=[]
d=[]

for j in range(l):
    a.append(int(A[j]))
n=a[0]    
A_s=np.sort(a[1:])    
k_l=len(B)-1
for i in range (k_l):
    k_new=int(B[i+1])
    d.append(BinSearch(0,l-2,A_s,k_new))
for i in range (len(d)):
    print(d[i],end=' ')    
    
    
