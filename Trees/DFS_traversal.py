 class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preorder_dfs(root):
    res = []

    def go(node):
        if not node:
            return
        res.append(node.val)
        go(node.left)
        go(node.right)

    go(root)
    return res


def inorder_dfs(root):
    res = []

    def go(node):
        if not node:
            return
        go(node.left)
        res.append(node.val)
        go(node.right)

    go(root)
    return res


def postorder_dfs(root):
    res = []

    def go(node):
        if not node:
            return
        go(node.left)
        go(node.right)
        res.append(node.val)

    go(root)
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

    print("Pre-order traversal: root->left->right", preorder_dfs(n1))    # [3, 5, 12, 2, 10]
    print("In-order traversal: left->root->right", inorder_dfs(n1))    # [12, 5, 2, 3, 10]
    print("Post-order traversal: left->right->root", postorder_dfs(n1))  # [12, 2, 5, 10, 3]
