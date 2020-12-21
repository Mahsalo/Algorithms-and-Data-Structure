#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 10:45:34 2020

@author: mahsa
"""

class Solution:
    def color (self,image,r,c,source,sr,sc,newColor):
        if sr<0 or sc<0 or sr>r-1 or sc>c-1:
            return
        if image[sr][sc] != source:
            return
        image[sr][sc]=newColor
        self.color (image,r,c,source,sr-1,sc,newColor)
        self.color (image,r,c,source,sr+1,sc,newColor)
        self.color (image,r,c,source,sr,sc-1,newColor)
        self.color (image,r,c,source,sr,sc+1,newColor)
    
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if image[sr][sc]==newColor:
            return image
        r = len(image)
        c = len(image[0])
        source = image[sr][sc] #old value of the source pixel
        
        self.color(image,r,c,source,sr,sc,newColor)
        return image