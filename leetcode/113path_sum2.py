class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def pathSum(self, root, _sum):
        def helper(curr_node, curr_solution, all_solution, total):
            if curr_node.left is None and curr_node.right is None:
                if total + curr_node.val == _sum:
                    all_solution.append(curr_solution[:])
                return
            if curr_node.left:
                curr_solution.append(curr_node.left.val)
                helper(curr_node.left, curr_solution, all_solution, total + curr_node.val)
                curr_solution.pop()
            if curr_node.right:
                curr_solution.append(curr_node.right.val)
                helper(curr_node.right, curr_solution, all_solution, total + curr_node.val)
                curr_solution.pop()
        res = []
        if root is not None:
            helper(root, [root.val], res, 0)
        return res

if __name__ == "__main__":
    
