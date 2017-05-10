class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def closestKValues(self, root, target, k):
        def inorder(node, reverse, target, path):
            if node is None:
                return
            
            if reverse: inorder(node.right, reverse, target, path)
            else: inorder(node.left, reverse, target, path)

            if (reverse and node.val <= target) or (not reverse and node.val > target):
                return
            path.append(node.val)

            if reverse: inorder(node.left, reverse, target, path)
            else: inorder(node.right, reverse, target, path)

        predecessors = []
        successors = []
        inorder(root, False, target, predecessors)
        inorder(root, True, target, successors)

        res = []
        for i in xrange(k):
            if not predecessors:
                res.append(successors.pop())
            elif not successors:
                res.append(predecessors.pop())
            elif abs(predecessors[-1] - target) < abs(successors[-1] - target):
                res.append(predecessors.pop())
            else:
                res.append(successors.pop())
        return res
                
