#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 20:19:51 2020

@author: mahsa
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        s = [0]*(n+1)
        s[0] = 1
        s[1] = 1
        for i in range(2,n+1):
            s[i] = s[i-1] + s[i-2]
        return s[n]    
            
     