class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def verticalOrder(self, root):
        def bfs(node, order):
            queue = deque([(node, order)])
            while queue:
                length = len(queue)
                for _ in xrange(length):
                    node, order = queue.popleft()
                    if order < 0:
                        if order < -len(left_res):
                            left_res.append([node.val])
                        else:
                            left_res[-order-1].append(node.val)
                    else:
                        if order >= len(right_res):
                            right_res.append([node.val])
                        else:
                            right_res[order].append(node.val)
                    if node.left:
                        queue.append((node.left, order - 1))
                    if node.right:
                        queue.append((node.right, order + 1))

        left_res = []
        right_res = []
        if root:
            bfs(root, 0)
        return left_res[::-1] + right_res
        
