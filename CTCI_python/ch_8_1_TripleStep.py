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
        s[2] = 2
        for i in range(3,n+1):
            s[i] = s[i-1] + s[i-2] + s[i-3]
        return s[n]  

n =4
obj = Solution()
print(obj.climbStairs(3))    
            
     