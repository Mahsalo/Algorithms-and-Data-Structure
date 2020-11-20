#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 09:19:57 2020

@author: mahsa
"""
class Solution:
    def compress(self, chars: List[str]) -> int:
        l = len(chars)
        count_vec = []
        s = ""
        ind = 0
        tmp = chars.copy()
        j=0
        chars.clear()
        for cnt, i in enumerate(tmp):
            if cnt == 0:
                prev = i
                ind = 1
            else:
                if prev== i:
                    ind +=1
                else:
                    count_vec.append(ind)
                    s = s+prev+str(ind)
                    if ind<=9:
                        space=list(prev+str(ind))
                    else:
                        lv=list(prev)
                        space=lv+(list(str(ind))) 
                    if ind>1:    
                        chars[j:j+len(space)]=list(prev+str(ind))
                        j=j+len(space)
                    elif ind==1:
                        chars[j:j+1]=prev  
                        j=j+1  
                    prev = i
                    ind=1

        if cnt == len(tmp)-1: 
            count_vec.append(ind)
            s = s+prev+str(ind)
            if ind<=9:
                space=list(prev+str(ind))
            else:
                lv=list(prev)
                space=lv+(list(str(ind))) 
            if ind>1:    
                chars[j:j+len(space)]=list(prev+str(ind))
                j=j+len(space)
            elif ind==1:
                chars[j:j+1]=prev  
                j=j+1    
  

        if len(chars)>=len(tmp):
            chars = tmp   
        return len(chars)    
                    
