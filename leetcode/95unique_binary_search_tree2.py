class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def generateTrees(self, n):
        def helper(nums):
            trees = []
            if len(nums) == 0:
                trees.append(None)
            elif len(nums) == 1:
                trees.append(TreeNode(nums[0]))
            else:
                for i in xrange(len(nums)):
                    left_nums = nums[:i]
                    right_nums = nums[i+1:]
                    left_trees = helper(left_nums)
                    right_trees = helper(right_nums)
                    
                    for left_tree in left_trees:
                        for right_tree in right_trees:
                            root = TreeNode(nums[i])
                            root.left = left_tree
                            root.right = right_tree
                            trees.append(root)
            return trees
        if n == 0:
            return []
        return helper(range(1, n+1))

    #Solution2, more concised version, from forum
    def generateTrees2(self, n):
        def helper(start, end):
            res = []
            for i in range(start, end):
                left_trees = helper(start, i)
                right_trees = helper(i+1, end)
                for left_tree in (left_trees if len(left_trees) else [None]):
                    for right_tree in (right_trees if len(right_trees) else [None]):
                        root = TreeNode(i)
                        root.left = left_tree
                        root.right = right_tree
                        res.append(root)
            return res
        return helper(1, n+1)

if __name__ == "__main__":
    sol = Solution()
    print sol.generateTrees2(3)
                    

            
            
