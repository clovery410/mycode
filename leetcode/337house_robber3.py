class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def rob(self, root):
        def dfs(root, status):
            if root is None:
                return 0
            elif (root, status) in cache:
                return cache[(root, status)]
            if not status:
                left_sum = dfs(root.left, True)
                right_sum = dfs(root.right, True)
                cache[(root, status)] = left_sum + right_sum
            else:
                curr_sum = dfs(root.left, False) + dfs(root.right, False) + root.val
                left_sum = dfs(root.left, True)
                right_sum = dfs(root.right, True)
                cache[(root, status)] = max(curr_sum, left_sum + right_sum)
            return cache[(root, status)]
        if root is None:
            return 0
        cache = {}
        return dfs(root, True)
