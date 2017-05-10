class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def convertToDLL(self, root):
        def helper(curr_node):
            if curr_node.left is not None:
                left_head, left_tail = helper(curr_node.left)
                left_tail.right = curr_node
            else:
                left_tail = None
                left_head = curr_node
            if curr_node.right is not None:
                right_head, right_tail = helper(curr_node.right)
                right_head.left = curr_node
            else:
                right_head = None
                right_tail = curr_node
            curr_node.left = left_tail
            curr_node.right = right_head

            return left_head, right_tail

        new_head, new_tail = helper(root)
        return new_head, new_tail

if __name__ == '__main__':
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)
    node7 = TreeNode(7)

    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node5.left = node7
    node3.right = node6

    sol = Solution()
    head, tail = sol.convertToDLL(node1)
    print head.val
    print head.right.val
    print head.right.right.val
    print tail.left.left.left.val
    print tail.left.left.val
    print tail.left.val
    print tail.val
    print head.right.right.right.right.right.right.val
    
