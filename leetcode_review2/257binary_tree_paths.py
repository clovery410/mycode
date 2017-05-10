class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def binaryTreePaths(self, root):
        def dfs(node, path):
            path.append(str(node.val))
            if node.left is None and node.right is None:
                res.append('->'.join(path))
                path.pop()
                return
            if node.left:
                dfs(node.left, path)
            if node.right:
                dfs(node.right, path)
            path.pop()

        res = []
        if root:
            dfs(root, [])
        return res

