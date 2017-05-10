class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def invertTree(self, root):
        def dfs(cur_root):
            if cur_root is None:
                return None
            left_child = cur_root.left
            right_child = cur_root.right
            cur_root.left = right_child
            cur_root.right = left_child
            dfs(left_child)
            dfs(right_child)
            return cur_root

        return dfs(root)
            
