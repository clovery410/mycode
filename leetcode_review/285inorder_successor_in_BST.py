class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        def searchBST(node):
            left_min = left_max = node.val
            right_min = right_max = node.val

            if node.left:
                left_min, left_max = searchBST(node.left)
            if node.right:
                right_min, right_max = searchBST(node.right)

            if left_max != node.val and left_max == p.val:
                self.res = node.val
            elif p.val == node.val and node.val != right_min:
                self.res = right_min
                
            return (left_min, right_max)

        self.res = None
        if root:
            searchBST(root)
        return self.res

    # solution2, use the property of BST
    def inorderSuccessor2(self, root, p):
        successor = None
        cur_node = root
        while cur_node:
            if p.val < cur_node.val:
                successor = cur_node.val
                cur_node = cur_node.left
            else:
                cur_node = cur_node.right
        return successor
                

if __name__ == "__main__":
    node5 = TreeNode(5)
    node3 = TreeNode(3)
    node8 = TreeNode(8)
    node2 = TreeNode(2)
    node1 = TreeNode(1)
    node4 = TreeNode(4)
    node6 = TreeNode(6)

    node5.left = node3
    node5.right = node8
    node3.left = node2
    node3.right = node4
    node8.left = node6
    node2.left = node1

    sol = Solution()
    print sol.inorderSuccessor(node5, node1)
    print sol.inorderSuccessor2(node5, node1)

    
            
                
                
