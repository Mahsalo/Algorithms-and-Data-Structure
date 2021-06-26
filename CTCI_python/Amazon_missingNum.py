#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 09:41:34 2021

@author: mahsa

Find the missing number in nums (it;'s in [0:n] but not in nums)
"""


class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        for i in range(n+1):
            if i not in nums:
                return i
           
                    
             