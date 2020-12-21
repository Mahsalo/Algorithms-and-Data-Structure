#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 16:38:26 2020

@author: mahsa
In this module I have implemented the Minimal Tree of a sorted array using binary search tree
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums):
        if len(nums) == 0 or nums ==None:
            return None
        def recursiveFunc(nums,l,r):
            if l>r:
                return None
            else:
                mid = (l+r)//2
                root = TreeNode(nums[mid])
                root.left = recursiveFunc(nums, l, mid-1)
                root.right = recursiveFunc(nums,mid+1,r)
                return root
            
        return recursiveFunc(nums,0,len(nums)-1)      


