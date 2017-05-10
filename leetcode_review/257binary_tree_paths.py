class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    #Solution1, recursive solution
    def binaryTreePaths(self, root):
        def dfs(node, cur_path):
            cur_path.append(str(node.val))
            if node.left is None and node.right is None:
                all_paths.append(''.join(cur_path))
                cur_path.pop()
                return
            cur_path.append("->")
            if node.left:
                dfs(node.left, cur_path)
            if node.right:
                dfs(node.right, cur_path)
            cur_path.pop()
            cur_path.pop()

        all_paths = []
        if root:
            dfs(root, [])
        return all_paths

    #solution2, use stack, iteration
    def binaryTreePaths2(self, root):
        all_paths = []
        stack = [(root, '')]
        while len(stack) > 0:
            cur_node, cur_path = stack.pop()
            if cur_node is not None:
                cur_path += str(cur_node.val)
                if cur_node.left is None and cur_node.right is None:
                    all_paths.append(cur_path)
                cur_path += '->'
                stack.append((cur_node.right, cur_path))
                stack.append((cur_node.left, cur_path))
        return all_paths

    #Solution3, use dictionary to record each path
    def binaryTreePaths3(self, root):
        all_paths = []
        stack = []
        paths = {}
        if root:
            stack.append(root)
            paths[root] = str(root.val)
        while len(stack) > 0:
            cur_node = stack.pop()
            if cur_node.left is None and cur_node.right is None:
                all_paths.append(paths[cur_node])
            if cur_node.left:
                paths[cur_node.left] = paths[cur_node] + '->' + str(cur_node.left.val)
                stack.append(cur_node.left)
            if cur_node.right:
                paths[cur_node.right] = paths[cur_node] + '->' + str(cur_node.right.val)
                stack.append(cur_node.right)
        return all_paths
            
            
if __name__ == "__main__":
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(5)

    node1.left = node2
    node1.right = node3
    node2.right = node4

    sol = Solution()
    print sol.binaryTreePaths(node1)
    print sol.binaryTreePaths2(node1)
    print sol.binaryTreePaths3(node1)
