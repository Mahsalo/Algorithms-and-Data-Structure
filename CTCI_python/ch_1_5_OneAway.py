#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 09:19:57 2020

@author: mahsa
"""
import numpy as np

s1=input()
s2=input()

def OneAway(s1,s2):
    l1 = len(s1)
    l2= len(s2)
    Ascii1 = [0]*256
    Ascii2 = [0]*256            
    for j in s1:
        Ascii1[ord(j)] +=1 
    for j in s2:    
        Ascii2[ord(j)] +=1
    Diff = abs(np.array(Ascii1)-np.array(Ascii2))
       
    if abs(len(s1)-len(s2))>1:
        return False
    else:
        if len(s1)==len(s2): ##there must be a replacement

            if sum(Diff)==2:
                return True
            else:
                return False
        
        else:##There must be deletion or insertion
            if sum(Diff)>1:
                return False
            else:
                return True
print(OneAway(s1,s2))            
