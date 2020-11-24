#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 12:57:10 2020

@author: mahsa: 
"""

def Conversion(A,B):##inputs are integers
    xorVal = A ^ B
    binVal = bin(xorVal)
    binVal.replace("0b","")
    l = list(binVal)
    cnt = 0
    for i in l:
        if i == '1':
            cnt +=1
    return cnt    

print(Conversion(29,15))    