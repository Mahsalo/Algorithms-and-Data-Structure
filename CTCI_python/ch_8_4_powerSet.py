#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 20:58:38 2020

@author: mahsa
"""

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        Res = []
        tmp = nums
        wierd = 15.5
        for j in range(len(nums)):
            if nums[j]==0:
                nums[j]=wierd

        for i in range (2**n):
            st_bin = bin(i)[2:]
            #format(st_bin, "#0"+str(n+2)+"b") 
            #st_bin.replace("0b","")
            if len(st_bin) != n:
                ls = list(st_bin)
                ls.reverse()
                for y in range(n-len(st_bin)):
                    ls.append('0')
                ls.reverse()
                st_bin = ls    
            else:
                st_bin = list(st_bin)
            #[int(val) for val in st_bin]
            L = [int(st_bin[j])*nums[j] for j in range(n)] 
            Lc = L.copy()
            for k in range(len(L)):
                if L[k]==0:
                    Lc.remove(L[k])
                    
            for k in range(len(Lc)):
                if Lc[k]==wierd:
                    Lc[k]=0
            Res.append(Lc)
        
        return Res