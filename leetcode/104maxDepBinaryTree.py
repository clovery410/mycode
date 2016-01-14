class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxDepth(self, root):
        # if root is None:
        #     return 0
        # s = list()
        # s.append(root)
        # dep = 0
        # while len(s) != 0:
        #     top = s.pop()
        #     dep += 1
        #     if top.right is not None:
        #         s.append(top.right)
        #     if top.left is not None:
        #         s.append(top.left)
        # return dep

        def superb_depth(root):
            if root is None:
                return 0
            else:
                return max(superb_depth(root.left), superb_depth(root.right)) + 1
        return superb_depth(root)

        def recur_depth(root, dep):
            if root is not None:
                dep = dep + 1
                if root.left is None and root.right is None:
                    return dep
                if root.left is None and root.right is not None:
                    return recur_depth(root.right, dep)
                if root.left is not None and root.right is None:
                    return recur_depth(root.left, dep)
                else:
                    return max(recur_depth(root.left, dep), recur_depth(root.right, dep))
            else:
                return 0
        return recur_depth(root, 0)


if __name__ == '__main__':
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)

    node1.left = node2
    node1.right = node3
    node3.right = node4
    node4.left = node5

    sol = Solution()
    d = sol.maxDepth(node1)
    print d
