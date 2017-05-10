# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        def dfs(node):
            if node is None or node == p or node == q:
                return node
            
            left_res = dfs(node.left)
            right_res = dfs(node.right)
            if left_res is None:
                return right_res
            elif right_res is None:
                return left_res
            else:
                return node

        return dfs(root)
