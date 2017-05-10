class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    # solution1, use global variable to update the count
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        def dfsGetSum(node, path_sum):
            path_sum += node.val
            if path_sum == sum:
                self.count += 1
                
            if node.left:
                dfsGetSum(node.left, path_sum)

            if node.right:
                dfsGetSum(node.right, path_sum)
                
        def dfs(node):
            if node:
                dfsGetSum(node, 0)
                dfs(node.left)
                dfs(node.right)
                
        self.count = 0
        dfs(root)
        return self.count

    # does not use global variable, use recursive function with return value
    def pathSum2(self, root, target):
        def dfs(node, remain_sum):
            remain_sum -= node.val
            res = 0
            if remain_sum == 0:
                res += 1
            if node.left:
                res += dfs(node.left, remain_sum)
            if node.right:
                res += dfs(node.right, remain_sum)
            return res

        if root is None:
            return 0
        return dfs(root, target) + self.pathSum2(root.left, target) + self.pathSum2(root.right, target)
                
