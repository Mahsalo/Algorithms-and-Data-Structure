#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 09:19:57 2020

@author: mahsa
"""
import numpy as np
s=input()

def URLify1(s):
    new_s = " "
    for i in range(len(s)):
        if s[i]==" ":
           new_s=new_s+"%"
           new_s=new_s+"2"
           new_s=new_s+"0"
        else:
           new_s=new_s+s[i]
    return new_s       

print(URLify1(s))



