class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lcaBST(self, root, node1, node2):
        if node1.val == root.val or node2.val == root.val:
            return root.val
        if node1.val > node2.val:
            temp = node1
            node1 = node2
            node2 = temp
        if node1.val > root.val:
            return self.lcaBST(root.right, node1, node2)
        if node2.val < root.val:
            return self.lcaBST(root.left, node1, node2)
        else:
            return root.val

    def lcaBST_iterative(self, root, p, q):
        if p.val < q.val:
            l_node = p
            r_node = q
        else:
            l_node = q
            r_node = p

        while l_node.val > root.val:
            root = root.right
        while r_node.val < root.val:
            root = root.left
        return root.val

if __name__ == '__main__':
    node0 = TreeNode(0)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)
    node7 = TreeNode(7)
    node8 = TreeNode(8)
    node9 = TreeNode(9)

    node6.left = node2
    node6.right = node8
    # node2.left = node0
    # node2.right = node4
    # node4.left = node3
    # node4.right = node5
    # node8.left = node7
    # node8.right = node9

    sol = Solution()
    print sol.lcaBST(node6, node0, node3)
    print sol.lcaBST_iterative(node6, node0, node3)
