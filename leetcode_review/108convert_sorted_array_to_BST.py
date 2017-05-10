class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        def dfs(start, end):
            if start <= end:
                mid = (end - start) / 2 + start
                node = TreeNode(nums[mid])
                node.left = dfs(start, mid-1)
                node.right = dfs(mid+1, end)
                return node
            else:
                return None
            
        return dfs(0, len(nums) - 1)
        

if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7]
    sol = Solution()
    print sol.sortedArrayToBST(nums).right.left.val
        
