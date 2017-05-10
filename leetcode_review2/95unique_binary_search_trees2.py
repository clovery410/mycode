class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def generateTrees(self, n):
        def generate(start, end):
            if start == end:
                return [None]
            if start == end - 1:
                return [TreeNode(start)]
            res = []
            for root_val in xrange(start, end):
                left_children = generate(start, root_val)
                right_children = generate(root_val+1, end)
                for left_child in left_children:
                    for right_child in right_children:
                        root = TreeNode(root_val)
                        root.left = left_child
                        root.right = right_child
                        res.append(root)
            return res

        if n == 0:
            return []
        return generate(1, n+1)

    #solution2, rewrite the code previously learned from discuss
    def generateTrees2(self, n):
        def generate(start, end):
            res = []
            for root_val in xrange(start, end):
                left_children = generate(start, root_val)
                right_children = generate(root_val+1, end)
                for left_child in left_children if len(left_children) > 0 else [None]:
                    for right_child in right_children if len(right_children) > 0 else [None]:
                        root = TreeNode(root_val)
                        root.left = left_child
                        root.right = right_child
                        res.append(root)
            return res
        return generate(1, n+1)

if __name__ == "__main__":
    sol = Solution()
    print sol.generateTrees(3)
    print sol.generateTrees2(3)
            
