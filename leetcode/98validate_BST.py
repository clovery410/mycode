class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.ok = True

    def check(self, node):
        if node is None:
            return (None, None)
        mn, mx = node.val, node.val
        if node.left:
            mmn, mmx = self.check(node.left)
            if mmx >= node.val:
                self.ok = False
            if mmn < mn:
                mn = mmn
            if mmx > mx:
                mx = mmx

        if node.right:
            mmn, mmx = self.check(node.right)
            if mmn <= node.val:
                self.ok = False
            if mmn < mn:
                mn = mmn
            if mmx > mx:
                mx = mmx

        return (mn, mx)
            
    def isValidBST(self, root):
        self.check(root)
        return self.ok

if __name__ == '__main__':
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)

    node1.right = node2
    node2.right = node3

    s = Solution()
    print s.isValidBST(node1)
