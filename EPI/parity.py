#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 11:24:39 2021

@author: mahsa
In this module we are going to find the parity of a binary sequence
If odd number of ones, parity is 1 otherwise it's 0.
Time complexity of this method is O(logn)
"""


def parity(x):
    p = False
    while x!=0:
        x = x&(x-1) ##This term unsets the lower-most one, so we can unset all the ones in a sequence
        p = ~p
    return p
X=5
P=parity(X)
print('The parity of {a} is {b}'.format(a=X,b= ("odd" if P==-1 else "even") ))


    
