# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        curr_closest = abs(target - root.val)
        closest_val = root.val
        curr_node = root
        while curr_node:
            if curr_node.val == target:
                return curr_node.val
            if abs(target - curr_node.val) < curr_closest:
                closest_val = curr_node.val
                curr_closest = abs(target - curr_node.val)
            if curr_node.val < target:
                curr_node = curr_node.right
            elif curr_node.val > target:
                curr_node = curr_node.left
        return closest_val
