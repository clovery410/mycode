class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    #solution1, recursion solution
    def isSymmetric(self, root):
        def check(node1, node2):
            if node1 == None and node2 == None:
                return True
            if node1 == None or node2 == None:
                return False
            if node1.val == node2.val:
                return check(node1.left, node2.right) and check(node1.right, node2.left)
            else:
                return False

        if root:
            return check(root, root)
        return True

    #solution2, iterative solution
    def isSymmetric2(self, root):
        def insertAll(stack, node, isLeft):
            while node:
                stack.append(node)
                node = node.left if isLeft else node.right
                    
        stack1, stack2 = [], []
        insertAll(stack1, root, True)
        insertAll(stack2, root, False)

        while stack1 and stack2:
            cur1, cur2 = stack1.pop(), stack2.pop()
            if len(stack1) != len(stack2) or cur1.val != cur2.val:
                return False
            insertAll(stack1, cur1.right, True)
            insertAll(stack2, cur2.left, False)
            
        if stack1 or stack2:
            return False
        return True

    
