#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 19:02:26 2021

@author: mahsa
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prevNode = None
        nextNode = None
        cur = head
        
        while cur:
            nextNode = cur.next
            cur.next = prevNode
            prevNode = cur
            cur = nextNode
         
        return prevNode    