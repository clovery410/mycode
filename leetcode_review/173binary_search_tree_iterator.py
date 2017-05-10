class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator(object):
    def __init__(self, root):
        self.stack = []
        self.addLeftNodes(root)

    def hasNext(self):
        return True if self.stack else False

    def next(self):
        cur = self.stack.pop()
        self.addLeftNodes(cur.right)
        return cur.val

    def addLeftNodes(self, node):
        while node:
            self.stack.append(node)
            node = node.left

if __name__ == "__main__":
    node1 = TreeNode(5)
    node2 = TreeNode(3)
    node3 = TreeNode(8)
    node4 = TreeNode(1)
    node5 = TreeNode(4)
    node6 = TreeNode(6)
    node7 = TreeNode(9)

    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.left = node6
    node3.right = node7

    bst = BSTIterator(node1)
    print bst._next()
    print bst._next()
    print bst._next()
    print bst._next()
    print bst._next()
    print bst._next()
    print bst._next()
    print bst.hasNext()
