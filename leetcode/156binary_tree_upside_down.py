class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def upsideDownBinaryTree(self, root):
        def dfs(node):
            if node.left is None and node.right is None:
                return (node, node)
            new_root, right_most = dfs(node.left)
            right_most.left = node.right
            right_most.right = node
            node.left = None
            node.right = None
            return (new_root, node)

        if root:
            return dfs(root)[0]
        else:
            return None
