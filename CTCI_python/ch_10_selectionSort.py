#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 10:16:45 2020

@author: mahsa:
    Selection sort: avg. , worst, O(N^2) , memory : O(1)
    find the minimum value of the unsorted array
"""

def selection(arr):
    n = len(arr)
    for i in range (n):
        for j in range(i+1,n):
            if arr[i] >= arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    
    return arr
    
    
arr = [11,20,3,2,4,1,5,40]
print(selection(arr))    
