class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution(object):
    # This original version works really bad, the code is not clear at all!!! Need to improve..
    def sortedArrayToBST(self, nums):
        if nums == []:
            return None
        n = len(nums)
        head = TreeNode(nums[(n-1)/2])
        
        def addNext(node, start, end):
            if start >= end:
                return
            mid = (start + end) / 2
            left_mid = (start + mid - 1) / 2
            right_mid = (mid + end + 1) / 2
            if left_mid >= start and left_mid < mid:
                node.left = TreeNode(nums[left_mid])
                addNext(node.left, start, mid - 1)
            if right_mid <= end and right_mid > mid:
                node.right = TreeNode(nums[right_mid])
                addNext(node.right, mid + 1, end)
                
        addNext(head, 0, n-1)
        return head

    # Learnt form Discuss, recursive could always written in concise
    def more_concise_version(self, nums):
        def addNode(left, right):
            if left > right:
                return None
            if left == right:
                return TreeNode(nums[left])

            mid = (left + right) / 2
            root = TreeNode(nums[mid])
            root.left = addNode(left, mid-1)
            root.right = addNode(mid+1, right)

            return root
        return addNode(0, len(nums) - 1)
