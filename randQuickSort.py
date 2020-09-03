#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 18:07:18 2020

@author: mahsa
In this module, we try to improve the quick sort algorithm 
so that it would be  able to handle the case when there are too
many equal elements in the array, this case would be the worst 
case with O(n^2) for quick sort but we just solve it with 3 way partitioning

"""

import numpy as np
import random



def Partition(a,low,high):
    lt=low#smaller than pivot
    gt=high#larger than pivot
    i=low#scan from left
    pivot=a[low]
    
    while (i<=gt):
        if pivot>a[i]:
            a[i],a[lt]=a[lt],a[i]
            lt+=1
            i+=1
            
            
        elif pivot<a[i]:
              a[i],a[gt]=a[gt],a[i]
              gt-=1
        else:
               i=i+1
    return lt,gt
        
def randQuickSort(a,low, high):
        if low >= high:
            return
    
        pivot_loc=random.randint(low,high) 
        a[low],a[pivot_loc]=a[pivot_loc],a[low]#first element is the pivot
        lt,gt=Partition(a,low,high)
        randQuickSort(a,low,lt-1)
        randQuickSort(a,gt+1,high)

    
n=int(input())
a=input()
a=a.split()
A=[]
for i in range(len(a)):
    A.append(int(a[i]) ) 
    
randQuickSort(A,0,n-1)
#quick_sort(A,0,n-1)
for i in range (n):
    print(A[i],end=' ')



