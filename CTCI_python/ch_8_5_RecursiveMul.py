#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 11:55:44 2020

@author: mahsa: Divide the smaller value by half then multiply by 2 afterwards
"""

def RecMultHelp(smaller,bigger):

    
    smaller = smaller //2
    if smaller ==0 :
        return bigger
    
    res = RecMultHelp(smaller,bigger)
    res = res + bigger
    return res
    
def RecMult(a,b):
    if a>b:
        bigger = a
        smaller = b
    else:
        bigger = b 
        smaller = a
    if smaller ==0:
        return 0
    if smaller == 1:
        return bigger
    if smaller % 2 ==0:
        res = RecMultHelp(smaller,bigger)*2
        return res
    else:
        return RecMultHelp(smaller,bigger)*2+bigger
        
    
    
a = 22
b = 8
c= 9
res1 = RecMult(a,b)
res2 = RecMult(a,c)

print("The Recursive Multiplication of {a} and {b} is {res1} ".format(a=a,b=b,res1=res1))
print("The Recursive Multiplication of {a} and {c} is {res2} ".format(a=a,c=c,res2=res2))

    