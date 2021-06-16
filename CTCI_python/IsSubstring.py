#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 17:30:53 2021

@author: mahsa
"""

def IsSubstring(s1,s2):
    w1 = len(s1)
    w2 = len(s2)
    
    for i in range(0,w1-w2+1):
        window = s1[i:i+w2]
        
        if window == s2:
            return True
        
    return False    
    

    
s1 = "mahsajoon"
s2 = "sal"    
print("s2 is the substring of s1?:",IsSubstring(s1,s2))    