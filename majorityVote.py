#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 12:48:06 2020

@author: mahsa
In this module, we try to find the maximum vote in an array
using divide and conquer method with runtime O(nlog n), if the 
frequency of occurance of any element in an array is more than n/2
that element wins the maximum vote

We can also implement the Moore method to achieve an even better
performance with O(n)   
"""

import numpy as np
def GetFreq(array,key):
    count=0
    for i in range (len(array)):
        if array[i]==key:
            count=count+1
    return count        
    
    
def FindMost(a,low,high,n):
    N=len(a)
    if low==high:
        return a[low]
        
    mid=int(low+np.floor((high-low)/2))
    l=FindMost(a,low,mid,n)
    r=FindMost(a,mid+1,high,n)

    if l==r:
        return l
    
    lcount=GetFreq(a,l)
    rcount=GetFreq(a,r)
    
    if lcount>n/2:
        return l
    
    if rcount>n/2:
            return r
    return None
          
n=int(input())
a=input()
a=a.split()
for i in range(len(a)):
    a[i]=int(a[i])
result=FindMost(a,0,n-1,n)

###In order to simplify it we can sort the array first
a_s=np.sort(a)
mid=int(np.floor(len(a_s)/2))
pivot=a_s[mid]
r=GetFreq(a_s,pivot)

if r>n/2:
    result1=1
else:
    result1=None
### You can replace result1 with result    
if result1==None:
    print(0)
else:
    print(1)
