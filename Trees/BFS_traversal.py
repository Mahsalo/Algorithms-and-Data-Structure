### Level by level

from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def bfs_algo(root):
    if not root:
        return []

    res = []
    q = deque([root])  # Store TreeNode objects, not node.val

    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node.val)
            if node.left:
                q.append(node.left)    # Push TreeNode, not node.left.val
            if node.right:
                q.append(node.right)  # Push TreeNode, not node.right.val

        res.append(level)

    return res


if __name__ == "__main__":
    n1 = TreeNode(3)
    n2 = TreeNode(5)
    n3 = TreeNode(2)
    n4 = TreeNode(10)
    n5 = TreeNode(12)

    n1.left = n2
    n1.right = n4
    n2.left = n5
    n2.right = n3

    print("BFS traversal: level by level", bfs_algo(n1))  # [[3], [5, 10], [12, 2]]
