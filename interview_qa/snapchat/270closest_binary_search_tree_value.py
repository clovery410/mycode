class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def closestValue(self, root, target):
        def dfs(node):
            if abs(node.val - target) < abs(self.candidate - target):
                self.candidate = node.val
                
            if node.val == target:
                return
            if node.val > target and node.left:
                dfs(node.left)
            elif node.val < target and node.right:
                dfs(node.right)
                
        self.candidate = root.val
        dfs(root)
        return self.candidate
    
