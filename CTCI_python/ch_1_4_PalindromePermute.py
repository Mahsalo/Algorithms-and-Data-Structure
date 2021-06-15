#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 09:19:57 2020

@author: mahsa
"""

class Solution:
    
    def Normalize(s):
        return s.replace(" ","")
    
    
    def canPermutePalindrome(self, s1: str) -> bool:
        Ascii = [0]*256
        cnt_odd=0
        cnt_even=0
        cnt_one=0
        
        s=Normalize(s1) ###remove the spaces
        for i in range(len(s)):
            Ascii[ord(s[i])]+=1
        for j in range(len(Ascii)):
            if Ascii[j]%2 == 1:
                cnt_odd+=1
            if Ascii[j]%2 == 0:
                cnt_even+=1
            if Ascii[j]==1:
                cnt_one+=1    
        if len(s)%2==0: 
            if cnt_odd==0:
                return True
            else:
                return False
        else:
            if cnt_odd>0 and cnt_one>1:
                return False
            if cnt_odd==1:
                return True
            
