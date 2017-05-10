class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.parent = None

class Solution(object):
    def common_ancestor(self, root, p, q):
        if p == root or q == root:
            return root
        
        p_parent = []
        q_parent = []
        curr_p, curr_q = p, q
        while curr_p:
            p_parent.append(curr_p)
            curr_p = curr_p.parent
        while curr_q:
            q_parent.append(curr_q)
            curr_q = curr_q.parent

        ret = None
        p_par = q_par = None
        while len(p_parent) > 0 and len(q_parent) > 0:
            p_par = p_parent.pop()
            q_par = q_parent.pop()
            if p_par == q_par:
                ret = p_par
            else:
                break
        return ret

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
node3.right = node6
node5.parent = node2
node4.parent = node2
node6.parent = node3
node2.parent = node1
node3.parent = node1

sol = Solution()
result = sol.common_ancestor(node1, node5, node4)
print result.val
