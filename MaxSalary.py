#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 19:37:29 2020

@author: mahsa

In this module we try to find the best pattern of given digits so that it will 
represent thebiggest value possible.

"""
import numpy as np

def IsGreaterEqual(a,b):
    A=int( str(a)+str(b))
    B=int( str(b)+str(a))
    if A>=B:
        return True
    else:
        return False
    
    
n=input()
Digits=input()
Digits=Digits.split()
Digits=np.array(Digits).astype(int)
i=0
answer=[]
while len(Digits):
    maxDigit=-1000
    for d in Digits:
       
        if maxDigit<0:
            maxDigit=d
        else:
            if IsGreaterEqual(d,maxDigit)==True:
                maxDigit=d 
                
    answer.append(maxDigit)
    Digits=list(Digits)
    Digits.remove(maxDigit)##make it a list to just remove the first occurance
print(*answer, sep = "")

        
            
    
