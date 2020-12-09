#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 10:33:43 2020

@author: mahsa: We would like to find the index at which A[i] = i 
We can use the Brute Force algorithm when the array is not sorted or has repetitions
We can use Binary search method when the array is sorted without repetitions
"""


L2 = [-2,-1,2,2,5,6,7,8] ###sorted with repetitons with magic index
L3 = [-2,-1,3,4,5,6]

### Brute force algorithm
flag =0
for i in range(len(L2)):
    if L2[i] == i:
        print('Magic index exist at index {i}'.format(i=i))
        flag = 1
        break
if flag==0:
    print('There is not magic number in the list')    



## Binary Search

L = [-2,-1,2,4,5,7, 10] ##sorted with magic index

def magicNum(arr,low,high):
    
    if high>=low:
        mid_ind = (low+high)//2 
        if arr[mid_ind] == mid_ind:
            return mid_ind
        
        else:
            if mid_ind>arr[mid_ind]:
                low = mid_ind + 1
                return magicNum(arr,low,high)
            else:
                high = mid_ind-1
                return magicNum(arr,low,high)
        
    else:
        return -1
    
low = 0
high = len(L)   
print(magicNum(L,low,high))
 

    
