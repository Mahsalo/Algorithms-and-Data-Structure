#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 12:57:10 2020

@author: mahsa: The input is an integer and the output is the longest sequence 
of 1s after one bit flip
"""

def Decimal2Binary(x):#the output is  a binary list
    q = x // 2
    r = []
    while q >=1:
        r.append(x%2)
        x = q
        q = x // 2
        if q ==1:
            r.append(x%2)
            r.append(q)
            break
    r.reverse()    
    return r

def BitFlip(num):
    b = Decimal2Binary(num) ## list
    l = len(b)
    ones = 0
    zeros = 0
    r = []
    print(b)
    for i in range(l):

        if i ==0:
            prev = curr = b[0]
        else:
            curr = b[i]
        print("p",prev)
        print("c",curr)
        if prev == curr :
            if curr == 1:
                ones +=1
                if i == l-1:
                    r.append((1,ones))
            else:
                zeros +=1
                if i ==l-1:
                    r.append((0,zeros))
        else:
            if prev == 1:
                tup_1 = (1,ones)
                r.append(tup_1)
                ones = 0
                zeros+=1
            else:
                tup_0 = (0,zeros)
                r.append(tup_0)
                zeros = 0  
                ones+=1

        prev = b[i]
        print('ones',ones)
        print('zeros',zeros)
        
    length = []
    print('r',r)
    for j in range(len(r)):
        if r[j] == (0,1):
            if j!=len(r)-1:
               
                length.append(r[j-1][1]+r[j+1][1]+1) 
                
            else:
                length.append(r[j-1][1]+1)
                
    length.sort(reverse=True)
    if length is not None:
        return length[0]
    else:
        return "ERROR"

print(BitFlip(1775))
            
                
        
        
        