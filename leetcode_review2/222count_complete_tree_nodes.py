class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def countNodes(self, root):
        def getHeight(node):
            h = 0
            while node:
                h += 1
                node = node.left
            return h

        if root is None:
            return 0
        cur_node = root
        count = 1
        while cur_node:
            if getHeight(cur_node.left) == getHeight(cur_node.right):
                cur_node = cur_node.right
                if cur_node:
                    count = count * 2 + 1
            else:
                cur_node = cur_node.left
                count = count * 2
        return count

