# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: # if empty
            return []

        q = deque([root])
        res = []
        
        while q:
            r = []
            for i in range(len(q)): ## each level
                n = q.popleft()
                r.append(n.val) # add to the level order results
                if n.left:
                    left = n.left
                    q.append(left) #add children to the Q if they exist
                if n.right:
                    right = n.right
                    q.append(right)
            res.append(r)
        return res


