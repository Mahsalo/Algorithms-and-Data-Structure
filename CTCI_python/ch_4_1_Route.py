#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 10:33:06 2020

@author: mahsa
In this module, we would like to check whether a specific edge exists between 
the source and the target or not
"""

from collections import defaultdict

class Graph:
    def __init__(self,vertices):
        self.V = vertices
        self.graph = defaultdict(list)
        
    def AddEdge(self,u,v):    
        self.graph[u].append(v)

    def isReachable(self,s,t):
        Q=[s]
        visited = [False]*self.V
        while Q:
            n = Q.pop(0) #take out the first element
            if n == t:
                return True
            for i in self.graph[n]:
                if visited[i] == False:
                    visited[i] = True
                    Q.append(i)
        return False             
   
obj = Graph(5) ##number of vertices are inputs
obj.AddEdge(0,1)
obj.AddEdge(0,2)
obj.AddEdge(1,3)
obj.AddEdge(2,4)

u , v = 0,4
s , t = 2,5

print('{u} and {v} have a common edge'.format(u=u,v=v),obj.isReachable(u,v))
print('{s} and {t} have a common edge'.format(s=s,t=t),obj.isReachable(s,t))





        
        
        