#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 12:27:01 2020

@author: mahsa
This module is written in order to implement Quick Sort with random pivot
My code could not consider the last element in the array so I added a wierd value and then removed it
"""
import numpy as np

def partition(A,low,high): #the first element is the piviot
    n = len(A) 
    p = low
    i, j= low, high ## j is bigger than the end of the array, acts as if inf.
    while(i<j): #once crosses it ends
        i, j= low, high ## j is bigger than the end of the array, acts as if inf.
        while(A[i]<=A[p]):
            i +=1
            if i>=high:
                break
    
        while(A[j]>=A[p]):
            j -=1   
            if j<=low:
                break
        if j>i:    
            A[i] , A[j]= A[j], A[i]
        if j == i:
            j = j-1
   
    piv_loc = j
    A[piv_loc],A[p] = A[p], A[piv_loc]
    return j
# def random_partition(arr,low,high):
#     pivot_loc = int(np.random.randint(low,high,1)) #include high as well
#     arr[pivot_loc],arr[low] = arr[low], arr[pivot_loc] #swap with the first element
#     return partition(arr,low,high)

def QuickSort(arr,low,high): 
    if low < high:
        J = partition(arr,low,high)
        QuickSort(arr,low,J)
        QuickSort(arr,J+1,high)
    
a = [9,0,1110,2,30,5,11,90,44,95,0,1,2,3,8]
wierd = max(a) +1
a.append(wierd)
QuickSort(a,0,len(a)-1)   
a.remove(wierd) 
print(a)    
    
    
    
    