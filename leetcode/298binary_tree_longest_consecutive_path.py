# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node, last_val, count, longest):
            if node is None:
                return max(count, longest)
            
            if node.val == (last_val + 1):
                count += 1
                longest = max(count, longest)
            else:
                count = 0
                
            left_max = dfs(node.left, node.val, count, longest)
            right_max = dfs(node.right, node.val, count, longest)
            return max(left_max, right_max)
        
        if root is None:
            return 0
        
        left_ret = dfs(root.left, root.val, 0, 0)
        right_ret = dfs(root.right, root.val, 0, 0)
        return max(left_ret, right_ret) + 1
