#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 14:42:58 2021

@author: mahsa

Needle in the haystack: First occurance of a substring inside a string
"""

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        w = len(needle)
        n = len(haystack)
        if w==0:
            return 0
        
        for i in range(n-w+1):
            sw= haystack[i:i+w]
            if sw == needle:
                return i
            
        return -1   