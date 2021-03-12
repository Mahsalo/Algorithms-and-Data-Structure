#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 19:28:14 2021

@author: mahsa
In this module, we are going to implement maximum profir for selling and buying once!
We should first buy cheap and then sell expensive alter. The runtime of the brute-force
algorithm is O(n^2) but we can reduce it to O(nlong) by divide-and-conquire and to O(n)
by using the difference with the minimum value seen thus far  
"""
def MaxStockProfit(x):
    min_stock = float("inf")
    max_profit = 0
    for price in x:
       diff = price-min_stock
       if diff<0:
           min_stock = price
       else:
           diff = price-min_stock
           if diff > max_profit:
               max_profit = diff
               
    return max_profit           
       
    
x=[310,315,275,295,260,270,290,230,255,250]
print(MaxStockProfit(x))    
