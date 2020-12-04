#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 12:18:10 2020

@author: mahsa
"""

class Solution:
    def str2digit(self, x)-> list: # x is only a char
        num = ord(x)-48
        return num
    def getDigits(self,x):
        summ = 0
        for i in range(len(x)):
            d = self.str2digit(x[i])
            summ += d*10**(len(x)-i-1)
          
        return summ
        
    def multiply(self, num1: str, num2: str) -> str:

        number1 = self.getDigits(num1)
        number2 = self.getDigits(num2)
        
        mul = number1*number2
        tmp = mul
        q = 1
        
        summ = 0
        j = 0
        r =[]
        while q:
            q = tmp // 10
            r.append(str(tmp % 10))
            summ +=(tmp%10)*10**j
            tmp = q
            j +=1
        return str(summ)