class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def rob(self, root):
        def dfs(node):
            if node.left is None and node.right is None:
                return (node.val, 0)

            include_left = exclude_left = include_right = exclude_right = 0
            if node.left:
                include_left, exclude_left = dfs(node.left)
            if node.right:
                include_right, exclude_right = dfs(node.right)

            # here, for the exclude value, need to do a max on children's include and exclude
            cur_exclude = max(include_left, exclude_left) + max(include_right, exclude_right)
            return (exclude_left + exclude_right + node.val, cur_exclude)

        if not root:
            return 0
        include_root, exclude_root = dfs(root)
        return max(include_root, exclude_root)
        
