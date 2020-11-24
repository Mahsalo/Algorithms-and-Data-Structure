#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 12:57:10 2020

@author: mahsa: We would like to swap the bits of even and odd locations bit 1 with 2, bit 3 with 4...
Hint: 1010101: Hex Rep. 1010101, 101010: Hex Rep. 0xAA
Each A=10=1010 4 bits, Each 5=101, 3 bits
I assume that the bit index starts from 1 not zero
"""

def PairSwap(num):
    
    odd_removal_mask = 0xAAAAAA
    even_removal_mask = 0x555555
    
    e_num = num & odd_removal_mask
    o_num = num & even_removal_mask
    
    ### shift the even num. to the right and the odd num. to the left
    
    return (e_num >> 1) | (o_num << 1)

x=172
y=bin(x)
z=bin(PairSwap(x))
print("The binary Rep. of {x} is {y} and it's bit swap is {z}".format(x=x,y=y,z=z))
    