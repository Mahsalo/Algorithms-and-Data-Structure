#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 13:14:04 2020

@author: mahsa
"""

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        dis = []
        for i in range (len(points)):
            X = points[i]
            x = X[0]
            y = X[1]
            dis.append(x**2 + y**2)
        s = sorted( (e,j) for j,e in enumerate(dis) )
        res = []
        for k in range (K):
            srt = s[k]
            index = srt[1]
            res.append(points[index])
        return res 