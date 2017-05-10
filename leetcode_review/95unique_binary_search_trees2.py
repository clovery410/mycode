class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def generateTrees(self, n):
        def buildTrees(s, e):
            roots = []
            for i in xrange(s, e+1):
                left_children = buildTrees(s, i-1)
                right_children = buildTrees(i+1, e)
                for l_child in left_children if len(left_children) > 0 else [None]:
                    for r_child in right_children if len(right_children) > 0 else [None]:
                        root = TreeNode(i)
                        root.left = l_child
                        root.right = r_child
                        roots.append(root)
            return roots
        return buildTrees(1, n)

if __name__ == "__main__":
    sol = Solution()
    print sol.generateTrees(3)
                
