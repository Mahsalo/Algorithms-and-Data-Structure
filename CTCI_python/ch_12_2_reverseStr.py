#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 18:03:49 2020

@author: mahsa
"""

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        mid_ind = len(s) // 2
        l = len(s)
        for i in range (mid_ind):
            tmp = s[i]
            s[i] = s[l-1-i]
            s[l-1-i] = tmp
        return s    