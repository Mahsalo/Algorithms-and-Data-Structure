#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 21:59:26 2020

@author: mahsa
"""

import numpy as np
string = input()

def isPalindrome(s):

        string=s
        string = string.lower()
        func = lambda ch: ch.isalnum()
        chars = list(filter(func,string))
        string=''.join(chars)
    
        if len(string)<=1:
            return True
        else:
            
            l = int(np.floor(len(string)/2))
            str1=string[0:l]
            str2=string[-l:]
            str3=str2[::-1]

            if str1 == str3:
                return True
            else:
                return False
    
print(isPalindrome(string))    
    