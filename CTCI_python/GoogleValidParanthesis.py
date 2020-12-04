#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 11:02:56 2020

@author: mahsa
"""

class Solution:
    def isValid(self, s: str) -> bool:
        right_brack = {'{','[','('}
        matching = {'}':'{',']':'[',')':'('}
        stack = []
        for i in range(len(s)):
            if s[i] in right_brack:
                stack.append(s[i])
            else:
                if len(stack) !=0:
                    if stack[-1]==matching[s[i]]:
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        if len(stack)==0:
            return True
        else:
            return False