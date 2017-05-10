class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        def helper(start, end):
            if end < start:
                return None
            root = TreeNode(preorder[self.idx])
            i = inorder.index(preorder[self.idx])
            self.idx += 1
            
            root.left = helper(start, i - 1)
            root.right = helper(i + 1, end)
            return root

        self.idx = 0
        return helper(0, len(inorder) - 1)
        



            
