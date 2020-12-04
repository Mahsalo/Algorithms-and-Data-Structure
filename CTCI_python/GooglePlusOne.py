#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 21:09:55 2020

@author: mahsa
"""

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry =0
        result = [0]*len(digits)
    
        for i in range(len(digits)):
            if i ==0:
                one = 1
                carry = 0
            else:
                one =0
            x = digits[len(digits)-i-1]+one+carry
            R = x % 10
            print(x)
            if x>=10:
               
                result[len(digits)-i-1]=R
                carry = 1
            else:
                result[len(digits)-i-1]=R
                carry = 0
        if carry ==1:
            result2 = [0]*(len(digits)+1)
            result2[1:len(result2)]=result
            result2[0]=carry
        else:
                result2 = result
        return result2 