class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

parents = []
q_parents = []
p_parents = []
        
def dfs(node, p, q):
    if node is None:
        return
    parents.append(node)
    if node == p:
        global p_parents
        p_parents = parents[:]
    if node == q:
        global q_parents 
        q_parents = parents[:]

    dfs(node.right, p, q)
    dfs(node.left, p, q)

    parents.pop()
    
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        dfs(root, p, q)
        p_len = len(p_parents)
        q_len = len(q_parents)

        i = 0
        while i < p_len and i < q_len:
            if p_parents[i] != q_parents[i]:
                return p_parents[i - 1]
            i += 1
        if q_len > p_len:
            return p_parents[-1]
        else:
            return q_parents[-1]


if __name__ =='__main__':
    node3 = TreeNode(3)
    node5 = TreeNode(5)
    node1 = TreeNode(1)
    node6 = TreeNode(6)
    node2 = TreeNode(2)
    node0 = TreeNode(0)
    node8 = TreeNode(8)

    node3.left = node5
    node3.right = node1
    node5.left = node6
    node5.right = node2
    node1.left = node0
    node1.right = node8

    sol = Solution()
    print sol.lowestCommonAncestor(node3, node3, node1).val

        
