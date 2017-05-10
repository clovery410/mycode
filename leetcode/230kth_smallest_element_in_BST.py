class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        def dfs(node, record):
            if node.left:
                dfs(node.left, record)
            record.append(node.val)
            if node.right:
                dfs(node.right, record)
                
        record = []
        dfs(root, record)
        return record[k-1]

    #second solution
    def kthSmallest2(self, root, k):
        self.k = k
        self.count = 0
        self.res = 0
        self.dfs(root)
        return self.res
    
    def dfs(self, node):
        if node.left:
            self.dfs(node.left)
        self.count += 1
        if self.count == self.k:
            self.res = node.val
            return
        if node.right:
            self.dfs(node.right)
            

if __name__ == '__main__':
    node1 = TreeNode(8)
    node2 = TreeNode(3)
    node3 = TreeNode(10)
    node4 = TreeNode(1)
    node5 = TreeNode(6)
    node6 = TreeNode(14)
    node7 = TreeNode(4)
    node8 = TreeNode(7)
    node9 = TreeNode(13)

    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.right = node6
    node5.left = node7
    node5.right = node8
    node6.left = node9
    
    sol = Solution()
#    print sol.kthSmallest(node1, 4)
    print sol.kthSmallest2(node1, 4)
