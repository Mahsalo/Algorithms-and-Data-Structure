#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 10:51:48 2021

@author: mahsa: This is sorting "Descendingly" you can reverse it for ascending sort
"""

class sortStack:
    def __init__(self,s1):
        self.s1 = s1 ###the unsorted stack is given to us
        self.s2 = []
    
    def sorting(self):
        
        for i in range(len(self.s1)):
            print('s1',self.s1)
            print('s2',self.s2)
            k = self.s1[-1]
            self.s1.pop()
            if i==0:
                self.s2.append(k)
                top = self.s2[-1]
                
            else:
                
                if  self.s2[-1]>= k:
                    self.s2.append(k)
                else:
                    ind=0
                    while (self.s2[-1]<k):
                        self.s1.append(self.s2[-1])
                        self.s2.pop()
                        ind +=1
                        if len(self.s2)==0:
                            break
                        
                    self.s2.append(k)
                    for  j in range(ind):
                        self.s2.append(self.s1[-1])
                        self.s1.pop()
                        
        return self.s2  

s = [12,45,3,7,2,89,0,11]
obj = sortStack(s)
print(obj.sorting())              
                
        