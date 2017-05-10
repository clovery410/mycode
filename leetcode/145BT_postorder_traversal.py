class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    #Solution 1, recursion, which is trivial
    def postorderTraversal(self, root):
        def dfs(node, res):
            if not node:
                return
            dfs(node.left, res)
            dfs(node.right, res)
            res.append(node.val)
        res = []
        dfs(root, res)
        return res

    #Solution2, iterative, as required by the question
    def postorderTraversal2(self, root):
        if root is None: return []
        stack = [root]
        res = []
        while stack:
            curr = stack.pop()
            if type(curr) != int:
                stack.append(curr.val)
                if curr.right:
                    stack.append(curr.right)
                if curr.left:
                    stack.append(curr.left)
            else:
                res.append(curr)
        return res

    #Solution3, second version of iterative solution, note differ from above solution is that first put left child into stack, then put right child into stack.
    def postorderTraversal3(self, root):
        if root is None: return []
        stack = [root]
        res = []
        while stack:
            curr = stack.pop()
            res.append(curr.val)
            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)
                
        res.reverse()
        return res

    #Come-up also implement pre-order traversal in iteration
    def preorderTraversal(self, root):
        if root is None: return []
        stack = [root]
        res = []
        while stack:
            curr = stack.pop()
            res.append(curr.val)
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)
        return res

    def inorderTraversal(self, root):
        if root is None: return []
        stack = [root]
        res = []
        while stack:
            curr = stack.pop()
            if type(curr) == int:
                res.append(curr)
            elif curr:
                stack.append(curr.right)
                stack.append(curr.val)
                stack.append(curr.left)
        return res

if __name__ == "__main__":
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

    sol = Solution()
    print sol.postorderTraversal(node1)
    print sol.preorderTraversal(node1)
    print sol.inorderTraversal(node1)
