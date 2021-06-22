#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 09:39:15 2020

@author: mahsa
This code is written to implement the counting sort
"""

def countingSort(arr):
    Ascii = [0]*256
    n = len(arr)
    d = dict() #creating an empty dictionary
    #d = {k:0 for k in set(arr)} #making an all-zero dictionary
    for i in range(n):
        Ascii[ord(str(arr[i]))] +=1
        #d[arr[i]] +=1
    for j in range(len(Ascii)):
        if Ascii[j] > 0:
            d[j] = Ascii[j]
    summ = 0
    new_d = {k:0 for k in d}        
    for i in d:        
        summ += d[i]  
        new_d[i] = summ
    shifted = {k:0 for k in d}
    j= 0 
    res = dict()
    for i in new_d:
        if j>0 :
            shifted[i] = res
            res = new_d[i]
        else: 
            res = new_d[i]
            j+=1
    wierd_val = 100        
    sorted_arr = [wierd_val] * n
    s = set(arr)        
    for k in s:
        cnt = d[ord(str(k))]
        j = shifted[ord(str(k))]
        if type(k)== str:
            sorted_arr[j:j+cnt-1] = list(k*cnt)
        else:
            sorted_arr[j:j+cnt-1] = [k]*cnt
    result = list(filter(lambda x: x != wierd_val,sorted_arr))
    return result  
            

arr1 = [5,0,2,2,4,6,8,1,1,1,2]
arr2 = ['s','r','a','a','y','s','t']
print('Sorting digits',countingSort(arr1))
print('Sorting characters',countingSort(arr2))

