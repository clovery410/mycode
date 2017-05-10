class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isValidBST(self, root):
        def check(node):
            left_min, left_max = check(node.left) if node.left else [node.val, None]
            right_min, right_max = check(node.right) if node.right else [None, node.val]
            if (left_max and left_max >= node.val) or (right_min and right_min <= node.val):
                self.isValid = False
            return [left_min, right_max]

        self.isValid = True
        if root:
            check(root)
        return self.isValid


