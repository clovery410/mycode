class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        def dfs(cur_node):
            if cur_node == p or cur_node == q:
                return cur_node
            elif (cur_node.val < p.val) != (cur_node.val < q.val):
                return cur_node
            elif cur_node.val < p.val:
                return dfs(cur_node.right)
            else:
                return dfs(cur_node.left)

        return dfs(root)
                
