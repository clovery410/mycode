class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def closestValue(self, root, target):
        def dfs(node):
            if node.val == target:
                self.res = node.val
                return
            if abs(node.val - target) < abs(self.res - target):
                self.res = node.val
            if node.val > target and node.left:
                dfs(node.left)
            elif node.val < target and node.right:
                dfs(node.right)
        self.res = root.val
        dfs(root)
        return self.res
