#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 12:57:10 2020

@author: mahsa: I compare the fractions with 1/2, 1/4 and ...
"""

def BinaryFractions(num):
    j=0
    if num >=1 or num<0:
        return "ERROR"
    else:
        frac = 0.5
        newNum =[]
        while(num>0):
            if num >= frac:
                newNum.append('1')
                num = num - frac
            else:
                newNum.append('0')
            frac= frac/2
            if j>31:
                #return "ERROR"
                break
            j+=1
        newS = "".join(newNum)
        newS = "0."+newS
        return newS            
    
x = 0.72
r = BinaryFractions(x)
print("The binary rep. of {x} is : {r}".format(x=x, r=r))    