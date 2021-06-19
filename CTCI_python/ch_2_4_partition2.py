# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        left = left_head = ListNode(0)
        right = right_head = ListNode(0)
        
        
        while head != None:
            if head.val<x:
                left.next = head
                left= left.next
            else:
                right.next = head
                right = right.next
                
            head = head.next  
        right.next = None
        left.next = right_head.next
        return left_head.next
                
            