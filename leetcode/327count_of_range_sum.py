class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self._sum = val
        self.left = None
        self.right = None

class SegmentTreeNode(object):
    def __init__(self, minVal, maxVal):
        self.minVal = minVal
        self.maxVal = maxVal
        self.count = 0
        self.left = None
        self.right = None
        
class Solution(object):
    #Solution1, wrong solution...
    def countRangeSum(self, nums, lower, upper):
        n = len(nums)
        count, index_range = 0, 0
        for num in nums:
            if num >= lower and num <= upper:
                count += 1
        s, e = 0, n-1
        range_sum = sum(nums)
        while s < e:
            two_sum = nums[s] + nums[e]
            if two_sum >= lower and two_sum <= upper:
                index_range = e - s + 1
                break
            elif two_sum < lower:
                s += 1
            else:
                e -= 1
        if index_range > 1:
            count += (index_range * (index_range - 1) / 2)
        return count

    #Solution2, also wrong solution...
    def countRangeSum2(self, nums, lower, upper):
        def insertNode(num, node):
            if node is None:
                node = TreeNode(num)
                if num >= lower and num <= upper:
                    self.count += 1
            else:
                node._sum += num
                if node._sum >= lower and node._sum <= upper:
                    self.count += 1
                if num < node.val:
                    node.left = insertNode(num, node.left)
                elif num > node.val:
                    node.right = insertNode(num, node.right)
            return node

        self.count = 0
        root = None
        for i in reversed(xrange(len(nums))):
            root = insertNode(nums[i], root)
        return self.count

    #Solution3
    # [-2, 5, -1] -> [-2, 3, 2] -> [-2, 2, 3]
    # s(j, i]: lower <= accum[i] - accum[j] <= upper -> accum[j] + lower <= accum[i] <= accum[j] + upper
    # so for each accum[j], we want to find out the number of all accum[i] which satisfy the above condition.
    def countRangeSum3(self, nums, lower, upper):
        if len(nums) <= 0:
            return 0
        accum = set()
        total, res = 0, 0
        for i in xrange(len(nums)):
            total += nums[i]
            accum.add(total)
        sorted_accum = sorted(accum)
        
        root = self.buildTree(sorted_accum, 0, len(sorted_accum) - 1)
        for i in reversed(xrange(len(nums))):
            self.updateTree(root, total)
            total -= nums[i]
            res += self.getCount(root, lower+total, upper+total)
        return res

    def buildTree(self, array, low, high):
        if low > high:
            return None
        node = SegmentTreeNode(array[low], array[high])
        if low < high:
            mid = (high - low) / 2 + low
            node.left = self.buildTree(array, low, mid)
            node.right = self.buildTree(array, mid + 1, high)
        return node

    def updateTree(self, node, num):
        if node is None:
            return
        if num >= node.minVal and num <= node.maxVal:
            node.count += 1
            self.updateTree(node.left, num)
            self.updateTree(node.right, num)

    def getCount(self, node, low_range, high_range):
        if high_range < node.minVal or low_range > node.maxVal:
            return 0
        if high_range >= node.maxVal and low_range <= node.minVal:
            return node.count
        left_count = self.getCount(node.left, low_range, high_range) if node.left else 0
        right_count = self.getCount(node.right, low_range, high_range) if node.right else 0
        return left_count + right_count


    #Solution4, use merge sort
    def countRangeSum(self, nums, lower, upper):
        if len(nums) <= 0:
            return 0
        total = 0
        accum = [0] * (len(nums) + 1)
        for i in xrange(len(nums)):
            total += nums[i]
            accum[i+1] = total
        
