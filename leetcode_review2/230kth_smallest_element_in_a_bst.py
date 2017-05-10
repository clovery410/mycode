class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        def insertAllLeft(node):
            while node:
                level_nodes.append(node)
                node = node.left
                
        level_nodes = []
        insertAllLeft(root)
        for x in xrange(k):
            top = level_nodes.pop()
            if x == k - 1:
                return top.val
            if top.right:
                insertAllLeft(top.right)
            
                

    #solution2, use binary search
    def kthSmallest2(self, root, k):
        def countNodes(node):
            if node is None:
                return 0
            return 1 + countNodes(node.left) + countNodes(node.right)

        count = countNodes(root.left)
        if k <= count:
            return self.kthSmallest2(root.left, k)
        elif k > count + 1:
            return self.kthSmallest2(root.right, k - count - 1)
        return root.val
