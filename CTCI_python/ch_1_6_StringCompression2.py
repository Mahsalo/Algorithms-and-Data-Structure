#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 12:36:39 2021

@author: mahsa
"""

def StringCompression(s):
    x = s[0]
    cnt = 0
    res = ""
    tmp = ""
    for i in range(len(s)):
        if s[i]==x:
            cnt +=1
            tmp = s[i]
        else:
            if cnt == 1:
                res = res+tmp
            else:
                res=res+tmp+str(cnt)
            cnt = 1
            x = s[i]
            tmp = x
            
    if i == len(s)-1:
            if cnt == 1:
                res = res+tmp
            else:
                res=res+tmp+str(cnt)
            
    return res        
            
            
    
    
    
    
    
    
    
s = input()  
print(StringCompression(s))  
