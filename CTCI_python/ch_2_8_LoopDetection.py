#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 11:06:07 2020

@author: mahsa: We would like to find the loop in the circular linked list

"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        s = set()
        while head is not None:
            if head in s:
                return True
            else:
                s.add(head)
                head = head.next
        pos = -1
        return False   