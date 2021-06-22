#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 19:14:03 2020

@author: mahsa
In this scipt, I have implmented the Bucket sort, which sorts digit by digit
"""

def Bucket(arr):
    max_val = max(arr)
    max_num = len(digits(max_val)) #number of iterations
    base = 10
    A = []
    for j in arr:
        diff = max_num-len(digits(j))
        left = '0'*diff
        c = left+str(j)
        A.append(c)
    A_tmp = A    
    for i in range(max_num):
        d = {dl : [] for dl in range(0,base)}   
        a = []
        for j in A_tmp:
            J = list(j)
            J_loc = J[max_num-i-1]
            a.append(J_loc)
            d[int(J_loc)].append(j)
        tmp = []    
        for k in d.values():
            if len(k) !=0:
                tmp.append(k)
        s1 = str(tmp)
        s2 = s1.replace('[',"")
        s3 = s2.replace(']',"")
        s4 = s3.replace(',',"")
        s5 = s4.replace("'","")
        i1 = 0
        new_ar = []
        while(i1<len(s5)):
            x= s5[i1:i1+max_num]
            new_ar.append(x)
            i1 += max_num+1 # we have some spaces in between

        A_tmp = new_ar   
    res = []
    for l in A_tmp:
        res.append(int(l))
    return res    
            


def digits(val):
    q = 1
    tmp = val
    digits = []
    while q !=0:
        q = tmp// 10
        r = tmp%10
        digits.append(r)
        tmp = q
    digits.reverse()    
    return digits 

arr = [110,23,425,12,23000,0,55]
print(Bucket(arr))
