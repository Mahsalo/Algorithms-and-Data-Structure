#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 21:59:26 2020

@author: mahsa
"""

import numpy as np
string = input()

def IsPalindrome(string):
    l = int(np.ceil(len(string)/2))
    str1=string[0:l-1]
    str2=string[l:len(string)]
    str3=str2[::-1]

    if str1 == str3:
        return True
    else:
        return False
    
print(IsPalindrome(string))    
    