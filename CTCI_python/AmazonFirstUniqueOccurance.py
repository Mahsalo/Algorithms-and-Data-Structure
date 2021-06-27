#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 18:05:16 2021

@author: mahsa
"""

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
      
        d = dict()
        for i in range(len(s)):
            if s[i] in d.keys():
                d[s[i]] +=1
            else:
                d[s[i]] = 1
        ind=[]
        for k in range(len(s)):
            if d[s[k]]==1:
                return k
        return -1
                    
        
        