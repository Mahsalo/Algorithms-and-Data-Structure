#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 18:06:02 2020

@author: mahsa
"""

filename = 'test.txt'
filepath = '/Users/mahsa/Desktop/'
 
Lines = ["This is the first line\n", "This is the second line\n","This is the 3rd line\n","This is the fourth line\n"]
L = len(Lines)
f = open(filepath+filename,'w')
f.writelines(Lines)
f.close()

k= 2
f2= open(filepath+filename)
R = f2.readlines()
f2.close()
l =len(Lines)
for i in range(k):
    print(R[l-1-i])
    


