#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 12:49:47 2021

@author: mahsa
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        i=j =0 ### i is the first pointer indicator, j is the second pointer indicator
        
        d = {}
        l = []
        for j in range(len(s)):
            if s[j] in d.keys():
                i = max(i,d[s[j]])
                
                
            d[s[j]] = j+1  
            l.append(j-i+1)
          
        print(l)
        if len(l)==0:
            return 0
        else:
            return max(l)    
                    