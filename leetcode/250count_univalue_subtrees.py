class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def countUnivalSubtrees(self, root):
        def dfs(node):
            if node.left is None and node.right is None:
                self.count += 1
                return True
            res = True
            if node.left:
                if not dfs(node.left) or node.left.val != node.val:
                    res = False
            if node.right:
                if not dfs(node.right) or node.right.val != node.val:
                    res = False

            if res:
                self.count += 1
            return res

        self.count = 0
        if root:
            dfs(root)
        return self.count
            
