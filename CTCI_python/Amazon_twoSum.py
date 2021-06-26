#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 09:41:34 2021

@author: mahsa

Given an integer array, find the indices of two values that sum up to a specific target. 
There is only one unique solution
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ind = dict()
        for i in range(len(nums)):
            diff = target-nums[i]
            if diff in ind:
                return [ind[diff],i]
            
            else:
                ind[nums[i]]=i