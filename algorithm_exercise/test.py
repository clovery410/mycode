class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def convertToDLL(self, root):
        def helper(node):
            if node.left is None and node.right is None:
                return (node, node)
            left_head = left_tail = right_head = right_tail = None
            if node.left:
                left_head, left_tail = helper(node.left)
                node.left = left_tail
            if node.right:
                right_head, right_tail = helper(node.right)
                node.right = right_head
            if left_tail:
                left_tail.right = node
            if right_head:
                right_head.left = node

            return (left_head, right_tail)

        new_head, new_tail = helper(root)
        return (new_head, new_tail)

if __name__ == '__main__':
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)

    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.right = node6

    sol = Solution()
    new_head, new_tail = sol.convertToDLL(node1)
    print new_head.val
    print new_head.right.val
    print new_head.right.right.val
    
