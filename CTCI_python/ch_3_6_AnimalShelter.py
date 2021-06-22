#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 11:30:11 2021

@author: mahsa
"""

class AnimalShelter:
    def __init__(self):
        self.dogs = ['d1','d2','d3','d4','d5']
        self.cats = ['c1','c2','c3','c4','c5','c6','c7']
        self.all = ['d1','d2','c1','c2','c3','d3','d4','d5','c4','c5','c6','c7']
        self.temp=[]
    def deqDog(self):  
        if len(self.dogs)!=0:
            dogToGo= self.dogs[0]
            print('Dog to go is',dogToGo)
            self.dogs.pop(0)
            d = self.all[0]
            for i in range(len(self.all)):
                if self.all[0]!=dogToGo:

                    self.temp.append(self.all[0])
                    self.all.pop(0)
                else:
                    self.all.pop(0)
                    
            for j in range(len(self.temp)):    
                self.all.append(self.temp[-1])
                self.temp.pop()
        else:
            print('No dogs left')
            
    def deqCat(self):  
        if len(self.cats)!=0:
            catToGo= self.cats[0]
            print('Cat to go is',catToGo)
            self.cats.pop(0)
            d = self.all[0]
            for i in range(len(self.all)):
                if self.all[0]!=catToGo:

                    self.temp.append(self.all[0])
                    self.all.pop(0)
                else:
                    self.all.pop(0)
            for j in range(len(self.temp)):    
                self.all.append(self.temp[-1])
                self.temp.pop()
        else:
            print('No cat left')
   
    def deqAny(self):
            self.all = self.all [::-1]
            print(self.all)
            x = self.all[0]
            print('the oldest animal to go is',x)
            self.all.pop(0)
            if x in self.dogs:
                self.dogs.pop(0)
            else:
                self.cats.pop(0)
                
obj = AnimalShelter()
obj.deqDog()    
obj.deqCat()            
obj.deqDog()  
obj.deqDog()  
obj.deqCat()  
obj.deqAny()            
        
        