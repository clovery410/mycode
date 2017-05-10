import collections
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    # do it recursively
    def lowestCommonAncestor(self, root, p, q):
        if root == None or root == p or root == q:
            return root
        left_res = self.lowestCommonAncestor(root.left, p, q)
        right_res = self.lowestCommonAncestor(root.right, p, q)
        if left_res is None:
            return right_res
        if right_res is None:
            return left_res
        return root

    # do it iteratively, use a haspmap to record the parent pointer
    def lowestCommonAncestor2(self, root, p, q):
        queue = collections.deque([root])
        parent = {root: None}
        while p not in parent or q not in parent:
            cur_node = queue.popleft()
            if cur_node.left:
                parent[cur_node.left] = cur_node
                queue.append(cur_node.left)
            if cur_node.right:
                parent[cur_node.right] = cur_node
                queue.append(cur_node.right)
                
        ancestors = set()
        while p:
            ancestors.add(p)
            p = parent[p]

        while q:
            if q in ancestors:
                return q
            q = parent[q]

if __name__ == "__main__":
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)

    node1.left = node2
    node1.right = node3
    node2.left = node4
    node3.right = node5

    sol = Solution()
    print sol.lowestCommonAncestor(node1, node2, node4).val
    print sol.lowestCommonAncestor2(node1, node2, node4).val
    
            
