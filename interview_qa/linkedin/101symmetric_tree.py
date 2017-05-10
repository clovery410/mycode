# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        def dfs(node1, node2):
            if (node1 == None) != (node2 == None):
                return False
            if node1 == node2 == None:
                return True
            if node1.val == node2.val:
                if dfs(node1.left, node2.right) and dfs(node1.right, node2.left):
                    return True
            return False

        if not root:
            return True
        return dfs(root.left, root.right)
        
