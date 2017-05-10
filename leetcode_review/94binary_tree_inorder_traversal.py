class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        res = []
        stack = []
        cur_node = root
        while cur_node:
            stack.append(cur_node)
            cur_node = cur_node.left
            
        while stack:
            top = stack.pop()
            res.append(top.val)
            cur_node = top.right
            while cur_node:
                stack.append(cur_node)
                cur_node = cur_node.left
        return res
        
