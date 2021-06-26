#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 16:48:10 2021

@author: mahsa

Find the common word that is not in the banned list
"""

class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        
        p = paragraph.lower()
      
        l = [str(i) for i in p if i in ["!","?","'",";",".",',']]
       
        for j in l:
            p = p.replace(str(j)," ")
        words=p.split()
        words = [str(i) for i in words ]  
        print(words)
        d = dict()
        for k in words:
            if k not in banned:
                if k not in d.keys():
                    d[k] = 1
                else:
                    d[k] +=1
        mxx = max(d.values())
        for j in d:
            if d[j] == mxx:
                return j
        
               