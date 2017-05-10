from collections import deque
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    #Solution1, DFS
    def minDepth(self, root):
        def dfs(node, depth):
            if node.left is None and node.right is None:
                return depth

            if node.left and node.right:
                return min(dfs(node.left, depth + 1), dfs(node.right, depth + 1))
            elif node.left:
                return dfs(node.left, depth + 1)
            else:
                return dfs(node.right, depth + 1)

        if root is None: return 0
        return dfs(root, 1)

    #Solution2, another DFS, more concised
    def minDepth2(self, root):
        def dfs(node):
            if not node:
                return 0
            if None in [node.left, node.right]:
                return max(dfs(node.left), dfs(node.right)) + 1
            else:
                return min(dfs(node.left), dfs(node.right)) + 1
        return 0 if root is None else dfs(root)
            
    #Solution3 BFS
    def minDepth3(self, root):
        if root is None: return 0
        queue = deque(((root, 1),))
        while queue:
            curr_node, curr_depth = queue.popleft()
            if curr_node.left is None and curr_node.right is None:
                return curr_depth
            if curr_node.left:
                queue.append((curr_node.left, curr_depth + 1))
            if curr_node.right:
                queue.append((curr_node.right, curr_depth + 1))
        return curr_depth

    #Solution4, second version of BFS, do not need to store all the node, store each level at once
    def minDepth4(self, root):
        depth, level = 0, [root]
        while level and level[0]:
            depth += 1
            for node in level:
                if not node.left and not node.right:
                    return depth
            level = [child_node for node in level for child_node in (node.left, node.right) if child_node]
        return depth

if __name__ == "__main__":
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)

    node1.left = node2
    node2.right = node3

    sol = Solution()
    print sol.minDepth4(node1)
        
