#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 18:48:40 2020

@author: mahsa
In this module we try to find the minimum number of times that a car needs a
refill if the destination is d miles away and a full-tank helps with m miles each time.
"n" is the number of stations available on the way 
"""
import numpy as np
#import pandas as pd

def minStation(d,m,n,Stations):
    factor=True
    i=0
    if m>=d:
        i=0
    else:
        while factor: 
            f=np.where(Stations<=m)
            f_s=np.sort(f)
            f_s=f_s[0]
            if len(f_s)!=0:
                f_max=f_s[-1]
                newS=Stations[f_max]
                i+=1
                Stations=np.setdiff1d(Stations,Stations[f])
                if len(Stations>0):
                    Stations-=newS

                if np.abs(newS-d)<=m:
                    factor=False
                else:
                     d-=newS
            else:
                  if d>m:
                      return -1
                  else:
                      return i
                  factor=False
          
    return  i       

d=int(input())
m=int(input())
n=int(input())
Slist=input()
Slist=Slist.split()
Stations=np.zeros((n,1))
for j in range (n):
    Stations[j]=int(Slist[j])
print(minStation(d,m,n,Stations))

