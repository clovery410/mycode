class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    # dfs search does not work since the left lower node may preceeds right higher node
    def verticalOrder(self, root):
        def dfs(node, col):
            if col >= 0:
                if col == len(right):
                    right.append([])
                right[col].append(node.val)
            else:
                if -1-col == len(left):
                    left.append([])
                left[-1-col].append(node.val)
            if node.left:
                dfs(node.left, col-1)
            if node.right:
                dfs(node.right, col+1)

        left = []
        right = []
        if root:
            dfs(root, 0)

        return left[::-1] + right

    # use bfs search to do it
    def verticalOrder(self, root):
        if not root:
            return []
        cur_level = collections.deque([(root, 0)])
        left, right = [], []

        while cur_level:
            length = len(cur_level)
            for i in xrange(length):
                top_node, top_col = cur_level.popleft()
                if top_col >= 0:
                    if top_col == len(right):
                        right.append([top_node.val])
                    else:
                        right[top_col].append(top_node.val)
                else:
                    if -1-top_col == len(left):
                        left.append([top_node.val])
                    else:
                        left[-1-top_col].append(top_node.val)
                if top_node.left:
                    cur_level.append((top_node.left, top_col-1))
                if top_node.right:
                    cur_level.append((top_node.right, top_col+1))
                    
        return left[::-1] + right
        
if __name__ == "__main__":
    node3 = TreeNode(3)
    node9 = TreeNode(9)
    node8 = TreeNode(8)
    node4 = TreeNode(4)
    node0 = TreeNode(0)
    node1 = TreeNode(1)
    node7 = TreeNode(7)

    node3.left = node9
    node3.right = node8
    node9.left = node4
    node9.right = node0
    node8.left = node1
    node8.right = node7
    
    sol = Solution()
    print sol.verticalOrder(node3)
