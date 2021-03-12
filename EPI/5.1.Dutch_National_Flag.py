#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 12:18:43 2021

@author: mahsa
In this module, we are going to solve the Dutch National Flag problem.
There are 3 numbers (colors) and we want to sort them in linear time O(n) 
and without using extra space.

(1) Create a low pointer at the beginning of the array and a high pointer at the end of the array.
(2) Create a mid pointer that starts at the beginning of the array and iterates through each element.
(3) If the element at arr[mid] is a 2, then swap arr[mid] and arr[high] and decrease the high pointer by 1.
(4) If the element at arr[mid] is a 0, then swap arr[mid] and arr[low] and increase the low and mid pointers by 1.
(5) If the element at arr[mid] is a 1, don't swap anything and just increase the mid pointer by 1.
Continue until you hit the stop pointer
My mistake was that I dd not use the elif and else conditions at first
"""

def swap (x,y):
    tmp=x
    x=y
    y=tmp
    return 
def Dutch_Sort(x):
    start_ptr = 0
    end_ptr = len(x)-1
    mid_ptr = 0
    
    while True:
        if mid_ptr > end_ptr:
            break

        for i in range (len(x)):

            if x[mid_ptr] == 2:
                x[mid_ptr]= x[end_ptr]
                x[end_ptr] = 2
                end_ptr =end_ptr-1
            elif x[mid_ptr] == 0:
                x[mid_ptr]=x[start_ptr]
                x[start_ptr]=0
                start_ptr =start_ptr+1
                mid_ptr =mid_ptr+1
            else: 
                mid_ptr =mid_ptr+1
    return x


a= [1,2,0,1,1,1,0,2,1,2,2,0,0]
print(Dutch_Sort(a))      

