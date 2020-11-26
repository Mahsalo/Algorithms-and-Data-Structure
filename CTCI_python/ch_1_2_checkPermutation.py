#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 16:30:14 2020

@author: mahsa
"""

string1 = input()
string2 = input()

##First Method
def Permuted1(str1,str2):
    if len(str1)!=len(str2):
        return False
    else:
        s1 = sorted(str1)
        s2 = sorted(str2)
        
        if s1 == s2 :
            return True 
        else:
            return False
print(Permuted1(string1,string2))    

##Second Method: Use a dictionary

def Permuted2(str1,str2):
    Ascii1= [0]*256
    Ascii2= [0]*256
    if len(str1)!=len(str2):
        return False
    else:
        
        for i in str1:
            Ascii1[ord(i)]+=1
        for j in str2:
            Ascii2[ord(j)]+=1
        if Ascii1==Ascii2:
            return True
        else:
            return False
        
print(Permuted2(string1,string2))    
            
        
