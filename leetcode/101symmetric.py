class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    # def isSymmetric(self, root):
    #     if root is None:
    #         return True
    #     node = list()
    #     self.traverse(root, node)
    #     print node
    #     n = len(node)
    #     mid = n / 2
    #     print node
    #     for i in xrange(mid):
    #         if node[i] != node[n-1-i]:
    #             return False
    #     return True

    # def traverse(self, root, node):
    #     if root is None:
    #         node.append('null')
    #         return
    #     self.traverse(root.left, node)
    #     node.append(root.val)
    #     self.traverse(root.right, node)
    def isSymmetric(self, root):
        def _isSym(left, right):
            if left is None and right is None:
                return True
            if left is None and right is not None:
                return False
            if left is not None and right is None:
                return False
            if left.val == right.val:
                return _isSym(left.left, right.right) and _isSym(left.right, right.left)
            else:
                return False

        if root is None:
            return True
        return _isSym(root.left, root.right)


if __name__ == '__main__':
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(2)
    node4 = TreeNode(3)
    node5 = TreeNode(4)
    node6 = TreeNode(4)
    node7 = TreeNode(3)
    
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.left = node6
    node3.right = node7
    sol = Solution()
    result = sol.isSymmetric(node1)
    print result
