from collections import deque
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def minDepth(self, root):
        if root is None: return 0
        level = 1
        queue = deque([root])
        while queue:
            size = len(queue)
            for i in xrange(size):
                top = queue.popleft()
                if top.left is None and top.right is None:
                    return level
                if top.left:
                    queue.append(top.left)
                if top.right:
                    queue.append(top.right)
            level += 1
        return level

if __name__ == "__main__":
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node1.left = node2
    node2.left = node3
    node2.right = node4

    sol = Solution()
    print sol.minDepth(node1)
