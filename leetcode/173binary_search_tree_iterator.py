class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator(object):
    def __init__(self, root):
        self.level_nodes = []
        cur = root
        while cur:
            self.level_nodes.append(cur)
            cur = cur.left

    def hasNext(self):
        return True if self.level_nodes else False

    def _next(self):
        top = self.level_nodes.pop()
        if top.right:
            cur = top.right
            while cur:
                self.level_nodes.append(cur)
                cur = cur.left
        return top.val

if __name__ == "__main__":
    node1 = TreeNode(5)
    node2 = TreeNode(3)
    node3 = TreeNode(8)
    node4 = TreeNode(1)
    node5 = TreeNode(4)
    node6 = TreeNode(6)
    node7 = TreeNode(9)
