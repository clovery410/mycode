from collections import deque
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrder(self, root):
        if root is None:
            return []
        res = []
        queue = deque([root])
        while queue:
            length = len(queue)
            cur_level = []
            for i in xrange(length):
                top = queue.popleft()
                cur_level.append(top.val)
                if top.left: queue.append(top.left)
                if top.right: queue.append(top.right)
            res.append(cur_level)
        return res

if __name__ == "__main__":
    node1 = TreeNode(3)
    node2 = TreeNode(9)
    node3 = TreeNode(20)
    node4 = TreeNode(15)
    node5 = TreeNode(7)

    node1.left = node2
    node1.right = node3
    node3.left = node4
    node3.right = node5

    sol = Solution()
    print sol.levelOrder(node1)
