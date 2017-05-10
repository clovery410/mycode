class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def verticalOrder(self, root):
        def dfs(node, col, level, path):
            if node is None:
                return

            if col not in path:
                path[col] = [node.val,]
            else:
                path[col].append(node.val)

            dfs(node.left, col - 1, level + 1, path)
            dfs(node.right, col + 1, level + 1, path)

        path = {}
        dfs(root, 0, path)
        keys = []
        for key in path:
            if key > 0:
                path[key].reverse()
            keys.append(key)
        keys.sort()
        for i in xrange(len(keys)):
            keys[i] = path[keys[i]]
            
        print keys


if __name__ == "__main__":
    node3 = TreeNode(3)
    node9 = TreeNode(9)
    node20 = TreeNode(20)
    node15 = TreeNode(15)
    node7 = TreeNode(7)

    node3.left = node9
    node3.right = node20
    node20.left = node15
    node20.right = node7

    sol = Solution()
    sol.verticalOrder(node3)
    
