class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    #solution1, O(n) extra space to do inorder traversal and store every node
    #can be expanded into both predecessor and successor
    def inorderSuccessor(self, root, p):
        def inorder(node):
            if node:
                inorder(node.left)
                in_traverse.append(node)
                inorder(node.right)
        in_traverse = []
        inorder(root)
        if len(in_traverse) == 0: return None
        idx = in_traverse.index(p)
        return in_traverse[idx+1] if idx < len(in_traverse) - 1 else None

    #solution2, not use the array, just use the recursive stack extra space
    #can be expanded into both predecessor and successor
    def inorderSuccessor2(self, root, p):
        def inorder(node):
            l_min = l_max = None
            r_min = r_max = None
            if node.left:
                l_min, l_max = inorder(node.left)
            if node.right:
                r_min, r_max = inorder(node.right)
            if l_max == p:
                self.res = node
            if node == p:
                self.res = r_min
            if l_min is None: l_min = node
            if r_max is None: r_max = node
            return (l_min, r_max)
        
        self.res = None
        inorder(root)
        return self.res

    #solution3, since this question only ask for successor, so use stack to do inorder traversal iteratively, when cur == p, set the flag to True
    def inorderSuccessor3(self, root, p):
       stack = []
       cur = root
       flag = False
       while cur or len(stack) > 0:
           if cur:
               stack.append(cur)
               cur = cur.left
           else:
               cur = stack[-1].right
               if flag:
                   return stack.pop()
               else:
                   if stack.pop() == p: flag = True

    #solution4, because this is a BST, we can make use of this property
    def inorderSuccessor4(self, root, p):
        res, cur = None, root
        while cur:
            if cur.val > p.val:
                res = cur
                cur = cur.left
            else:
                cur = cur.right
        return res

    #solution5, based on the same idea, the predecessor can also be found
    def inorderPredecessor(self, root, p):
        res, cur = None, root
        while cur:
            if cur.val < p.val:
                res = cur
                cur = cur.right
            else:
                cur = cur.left
        return res
    
if __name__ == "__main__":
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)

    node3.left = node2
    node3.right = node5
    node2.left = node1
    node5.left = node4
    node5.right = node6

    sol = Solution()
    print sol.inorderSuccessor(node3, node5).val
    print sol.inorderSuccessor2(node3, node5).val
    print sol.inorderSuccessor3(node3, node5).val
    print sol.inorderSuccessor4(node3, node5).val
    print sol.inorderPredecessor(node3, node5).val
    
