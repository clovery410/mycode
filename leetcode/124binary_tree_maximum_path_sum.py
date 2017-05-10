class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxPathSum(self, root):
        def helper(node):
            if node is None:
                return 0
            left_max = helper(node.left)
            right_max = helper(node.right)

            # Update self.total_max value
            cur_max = node.val
            if left_max > 0:
                cur_max += left_max
            if right_max > 0:
                cur_max += right_max
            if cur_max > self.total_max:
                self.total_max = cur_max

            # Continue recurse
            if left_max > 0 or right_max > 0:
                return max(left_max, right_max) + node.val
            else:
                return node.val

        self.total_max = 0
        include_max = helper(root)
        return self.total_max if self.total_max > include_max else include_max
