class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def pathSum(self, root, _sum):
        def dfs(cur_node, cur_sum, cur_path, all_paths):
            if cur_node:
                cur_path.append(cur_node.val)
                if cur_sum == cur_node.val and not cur_node.left and not cur_node.right:
                    all_paths.append(cur_path[:])
                else:
                    dfs(cur_node.left, cur_sum - cur_node.val, cur_path, all_paths)
                    dfs(cur_node.right, cur_sum - cur_node.val, cur_path, all_paths)
                cur_path.pop()
        res = []
        dfs(root, _sum, [], res)
        return res

    #Solution2, iterable version
    def pathSum2(self, root, _sum):
        if not root:
            return []
        val, kids = root.val, (root.left, root.right)
        if any(kids):
            return [[val] + path
                    for kid in kids
                    for path in self.pathSum2(kid, _sum - val)]
        return [[val]] if val == _sum else []

    #Solution3, just recursion, no backtracing,  but slower than solution1 since this solution copies a new list at each recursion
    def pathSum3(self, root, _sum):
        def dfs(root, _sum, path, res):
            if root:
                if _sum == root.val and not root.left and not root.right:
                    res.append(path+[root.val])
                dfs(root.left, _sum - root.val, path + [root.val], res)
                dfs(root.right, _sum - root.val, path + [root.val], res)
        res = []
        dfs(root, _sum, [], res)
        return res

    #Solution4, dfs with iteration + stack, although iterative way saves the recursion time, but copying path costs a lot time
    def pathSum4(self, root, _sum):
        stack, res = [(root, _sum, [])], []
        while stack:
            node, cur_sum, path = stack.pop()
            if node:
                if not node.left and not node.right and cur_sum  == node.val:
                    res.append(path + [node.val])
                stack.append((node.right, cur_sum - node.val, path + [node.val]))
                stack.append((node.left, cur_sum - node.val, path + [node.val]))
        return res

if __name__ == "__main__":
    node1 = TreeNode(5)
    node2 = TreeNode(4)
    node3 = TreeNode(8)
    node4 = TreeNode(11)
    node5 = TreeNode(13)
    node6 = TreeNode(7)

    node1.left = node2
    node1.right = node3
    node2.left = node4
    node3.left = node5
    node3.right = node6

    sol = Solution()
    print sol.pathSum(node1, 20)
    print sol.pathSum2(node1, 20)
    print sol.pathSum3(node1, 20)
    print sol.pathSum4(node1, 20)
                    
