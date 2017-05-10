class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node, is_left):
            if node.left is None and node.right is None and is_left:
                return node.val
            res = 0
            if node.left:
                res += dfs(node.left, True)
            if node.right:
                res += dfs(node.right, False)
            return res
            
        if root:
            return dfs(root, False)
        else:
            return 0
