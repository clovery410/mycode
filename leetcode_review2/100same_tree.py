class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        def dfs(node1, node2):
            if node1 == None and node2 == None:
                return True
            if node1 == None or node2 == None:
                return False
            if node1.val == node2.val:
                return dfs(node1.left, node2.left) and dfs(node1.right, node2.right)
            else:
                return False

        return dfs(p, q)
            
