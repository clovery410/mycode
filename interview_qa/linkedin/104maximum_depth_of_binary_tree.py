# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # first approach
    def maxDepth(self, root):
        def dfs(node):
            if node.left is None and node.right is None:
                return 1
            left_depth = dfs(node.left) if node.left else 0
            right_depth = dfs(node.right) if node.right else 0
            return max(left_depth, right_depth) + 1

        return dfs(root) if root else 0

    # another approach
    def maxDepth2(self, root):
        def dfs(node, depth):
            if node is None:
                return depth
            return max(dfs(node.left, depth+1), dfs(node.right, depth+1))

        return dfs(root, 0)
            
