# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

ok = True

class Solution(object):
    def check(self, node):
        if node is None:
            return (None, None)
        global ok
        
        mn = node.val
        mx = node.val
        
        if node.left:
            mnn, mxx = self.check(node.left)
            if mxx >= node.val:
                ok = False
            if mnn < mn:
                mn = mnn
            if mxx > mx:
                mx = mxx
                
        if node.right:
            mnn, mxx = self.check(node.right)
            if mnn <= node.val:
                ok = False
            if mnn < mn:
                mn = mnn
            if mxx > mx:
                mx = mxx
    
        return (mn, mx)
        
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.check(root)
        return ok

s = Solution()
node1 = TreeNode(0)
node2 = TreeNode(-1)
node1.left = node2

print s.isValidBST(node1)