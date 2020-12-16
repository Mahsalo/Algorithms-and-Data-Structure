#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 09:49:36 2020

@author: mahsa:
    Bubble sort : runtime (avg_worst) O(n^2) and memory O(n)
    Bubble sort = swap sort
"""




def Bubble(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                
    return arr            
                
                
        



arr = [11,1,3,4,2,20,23]
print(Bubble(arr))