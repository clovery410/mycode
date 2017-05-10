from collections import deque
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    #Slow, use extra space...
    def isSymmetric(self, root):
        def check(node, is_left):
            res = []
            if node is None:
                return [None]
            res.extend([node.val])
            if is_left:
                res.extend(check(node.left, True))
                res.extend(check(node.right, False))
            else:
                res.extend(check(node.right, False))
                res.extend(check(node.left, True))
            return res
        return check(root.left, True) == check(root.right, False) if root else True

    #Solution2, make use of recursion, recursively check whether left.left symmetric right.right, and left.right symmetric right.left
    def isSymmetric2(self, root):
        def recurse(left, right):
            if left is None and right is None:
                return True
            elif left is None or right is None:
                return False
            elif left.val == right.val:
                return recurse(left.left, right.right) and recurse(left.right, right.left)
            else:
                return False
        return recurse(root.left, root.right) if root else True

    #Solution3, use iterative solution
    def isSymmetric3(self, root):
        if root is None:
            return True
        queue = deque([root, '#'])
        cur_level = []
        while queue:
            top = queue.popleft()
            if top is None:
                cur_level.append("None")
            elif top != '#':
                cur_level.append(top.val)
                queue.append(top.left)
                queue.append(top.right)
            else:
                if len(queue) > 0:
                    queue.append('#')
                if cur_level != cur_level[::-1]:
                    return False
                cur_level = []
        return True

if __name__ =="__main__":
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(2)
    node4 = TreeNode(3)
    node5 = TreeNode(3)
    node6 = TreeNode(4)
    node7 = TreeNode(3)

    node1.left = node2
    node1.right = node3
    # node2.left = node4
    node2.right = node5
    # node3.left = node6
    node3.right = node7

    sol = Solution()
    print sol.isSymmetric(node1)
    print sol.isSymmetric2(node1)
    print sol.isSymmetric3(node1)
    
