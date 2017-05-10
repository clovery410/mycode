class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def hasPathSum(self, root, total):
        def dfs(node, curr_total):
            curr_total += node.val
            if node.left is None and node.right is None:
                return True if curr_total == total else False
            elif node.left and dfs(node.left, curr_total):
                return True
            elif node.right and dfs(node.right, curr_total):
                return True
            else:
                return False

        if root:
            return dfs(root, total)
        return False
