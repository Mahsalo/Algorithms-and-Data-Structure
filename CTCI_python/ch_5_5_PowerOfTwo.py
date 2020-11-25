#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 15:58:45 2020

@author: mahsa: We would like to check if a number is a power of two or not?
"""

def IsPowerOfTwo(num):
    if num & (num-1) ==0 :
        return True
    else:
        return False

x=6
r=IsPowerOfTwo(x)
print("The integer {x} is a power of two: {r}".format(x=x, r=r))