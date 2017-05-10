class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    # solution1
    def lowestCommonAncestor(self, root, p, q):
        def dfs(node, search_node, path):
            if node is None:
                return []
            
            path.append(node)
            if node == search_node:
                res = list(path)
            else:
                res = dfs(node.left, search_node, path) or dfs(node.right, search_node, path)
            path.pop()
            return res

        p_parents = dfs(root, p, [])
        q_parents = dfs(root, q, [])
        i = 0
        while i < len(p_parents) and i < len(q_parents):
            if p_parents[i] != q_parents[i]:
                return p_parents[i-1]
            else:
                i += 1
        return p_parents[i-1]

    # solution2, use a hashmap to create a parent pointer
    def lowestCommonAncestor2(self, root, p, q):
        parent = {root: None}
        stack = [root]
        while p not in parent or q not in parent:
            cur_node = stack.pop()
            if cur_node.left:
                parent[cur_node.left] = cur_node
                stack.append(cur_node.left)
            if cur_node.right:
                parent[cur_node.right] = cur_node
                stack.append(cur_node.right)
                
        p_ancestors = set()
        while p:
            p_ancestors.add(p)
            p = parent[p]
        while q not in p_ancestors:
            q = parent[q]
        return q

    # solution3, check it recursively
    def lowestCommonAncestor3(self, root, p, q):
        if root is None or root == p or root == q:
            return root
        left_res = self.lowestCommonAncestor3(root.left, p, q)
        right_res = self.lowestCommonAncestor3(root.right, p, q)
        if left_res is None:
            return right_res
        elif right_res is None:
            return left_res
        else:
            return root
        
if __name__ == "__main__":
    sol = Solution()
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)

    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.left = node6
    
    print sol.lowestCommonAncestor(node1, node3, node6).val
    print sol.lowestCommonAncestor2(node1, node3, node6).val
    print sol.lowestCommonAncestor3(node1, node3, node6).val
