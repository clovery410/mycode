class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def rob(self, root):
        def dfs(node, flag):
            if (node, flag) in cache:
                return cache[(node, flag)]
            
            if node is None:
                cache[(node, flag)] = 0
            elif flag == False:
                cache[(node, flag)] = dfs(node.left, True) + dfs(node.right, True)
            else:
                include = dfs(node.left, False) + dfs(node.right, False) + node.val
                exclude = dfs(node.left, True) + dfs(node.right, True)
                cache[(node, flag)] = max(include, exclude)
            return cache[(node, flag)]

        cache = {}
        return dfs(root, True)

if __name__ == "__main__":
    node1 = TreeNode(3)
    node2 = TreeNode(2)
    node3 = TreeNode(7)
    node4 = TreeNode(3)
    node5 = TreeNode(1)

    node1.left = node2
    node1.right = node3
    node2.right = node4
    node3.right = node5

    sol = Solution()
    print sol.rob(node1)
    
