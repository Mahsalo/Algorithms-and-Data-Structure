#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 09:39:15 2020

@author: mahsa
This code is written to implement the Radix sort by using counting sort on each digit
"""

def countingSort(arr):
    Ascii = [0]*256
    B = [[]]*256
    n = len(arr)
    d = dict() #creating an empty dictionary
    for i in range(n):
        Ascii[ord(str(arr[i]))] +=1

        if len(B[ord(str(arr[i]))]) == 0:
            B[ord(str(arr[i]))] = [i]
        else:
            B[ord(str(arr[i]))].append(i) ## this keeps the indices
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
    ind = []
    for r in result:
        ind.append(B[ord(str(r))])

    return result , ind 


def digits(val):
    q = 1
    tmp = val
    digits = []
    while q !=0:
        q = tmp// 10
        print(q)
        r = tmp%10
        digits.append(r)
        tmp = q
    digits.reverse()    
    return digits  


                
def RadixSort(arr):
    maxx_val = max(arr)
    max_d = len(digits(maxx_val)) #maximum number of digits needed
    updated=[]
    for i in arr:
        diff = len(digits(i))-max_d
        if diff > 0:
            left = diff*'0'
            updated.append(left+str(i))
        else:
            updated.append(str(i))
    modif = [0]*len(arr)    ##modified
    for i in range(max_d):##for each pass
        new_arr = []
        for j in updated:
            l = list(j)
            last = l[len(l)-i-1] # last element
            new_arr.append(last)
        res_array, ind = countingSort(new_arr)  
        for k in range(len(updated)):
            ll = len(ind[k])
            if ll == 1:
                modif[k] = updated[ind[k]]



#print(digits(1243))
arr1 = [502,11,112,2,40,6,812,12,1,11,22]
arr1 = [5,1,2,2,0,6,8,2,1,1,2]

print('Sorting digits',countingSort(arr1))

