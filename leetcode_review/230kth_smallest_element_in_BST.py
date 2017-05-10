class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    # def __init__(self):
    #     self.res = None
    #     self.count = 0
        
    def kthSmallest(self, root, k):
        def inorder(root):
            if root.left:
                inorder(root.left)
            self.count += 1
            if self.count == k:
                self.res = root
            if root.right:
                inorder(root.right)

        self.res = None
        self.count = 0
        inorder(root)
        return self.res.val

if __name__ == "__main__":
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(9)

    node3.left = node2
    node3.right = node5
    node2.left = node1
    node5.left = node4

    sol = Solution()
    print sol.kthSmallest(node3, 5)
