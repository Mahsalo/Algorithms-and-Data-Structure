#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 15:04:26 2020

@author: mahsa
"""
##First Normalize the strings to lower case and delet the spaces
def normalized_str(str):
    str=str.replace(" ","")
    return str.lower()
##Method 1: use dictionaries
str_in = input()

str_in = normalized_str(str_in)

def IsUnique1(str_in):
    dictionary= dict()
    flag =True
    for i in str_in:
        if i in dictionary:
            flag =False
        else:
            dictionary[i]=1
        
    return flag    

print('First Method Says:',IsUnique1(str_in))   

##Second Method: Use sets
def IsUnique2(str_in):
    if(len(set(str_in))==len(str_in)):
        return True
    else:
        return False
print('Second Method Says:',IsUnique2(str_in))   
    



 
