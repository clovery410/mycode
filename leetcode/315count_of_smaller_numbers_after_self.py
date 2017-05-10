import sys
class TreeNode(object):
    def __init__(self, val, count):
        self.val = val
        self.count = count
        self.left = None
        self.right = None
        self.dup = 1
        
class Solution(object):
    #First try, but TLE...
    def countSmaller(self, nums):
        res = [0] * len(nums)
        self.mergeSort(list(enumerate(nums)), res, 0, len(nums) - 1)
        return res
    
    def mergeSort(self, enums, count, p, r):
        if p < r:
            mid = (r - p) / 2 + p
            self.mergeSort(enums, count, p, mid)
            self.mergeSort(enums, count, mid+1, r)
            self.merge(enums, count, p, mid, r)

    def merge(self, enums, count, p, q, r):
        n1 = q - p + 1
        n2 = r - q
        l1 = [(p+n1, sys.maxint)] * (n1+1)
        l2 = [(q+1+n2, sys.maxint)] * (n2+1)
        for i in xrange(n1):
            l1[i] = enums[p+i]
        for j in xrange(n2):
            l2[j] = enums[q+1+j]
        i = j = 0
        for k in xrange(p, r+1):
            if l1[i][1] <= l2[j][1]:
                enums[k] = l1[i]
                i += 1
            else:
                for x in xrange(i, n1):
                    count[l1[x][0]] += 1
                enums[k] = l2[j]
                j += 1

    #Solution2, more smart merge sort solution
    def countSmaller2(self, nums):
        def mergeSort(enum):
            half = len(enum) / 2
            if half:
                left, right = mergeSort(enum[:half]), mergeSort(enum[half:])
                m, n = len(left), len(right)
                i = j = 0
                while i < m or j < n:
                    if j == n or i < m and left[i][1] <= right[j][1]:
                        enum[i+j] = left[i]
                        smaller[left[i][0]] += j
                        i += 1
                    else:
                        enum[i+j] = right[j]
                        j += 1
            return enum
        smaller = [0] * len(nums)
        mergeSort(list(enumerate(nums)))
        return smaller

    #Solution3, use BST
    def countSmaller3(self, nums):
        def insertNode(num, node, res, pos, preSum):
            if node is None:
                node = TreeNode(num, 0)
                res[pos] = preSum
            elif node.val == num:
                node.dup += 1
                res[pos] = preSum + node.count
            elif node.val > num:
                node.count += 1
                node.left = insertNode(num, node.left, res, pos, preSum)
            else:
                preSum += node.dup + node.count
                node.right = insertNode(num, node.right, res, pos, preSum)

            return node
        
        res = [0] * len(nums)
        root = None
        for i in reversed(xrange(len(nums))):
            root = insertNode(nums[i], root, res, i, 0)
        return res
    
if __name__ == "__main__":
    nums = [5, 2, 6, 1, 3]
    sol = Solution()
    print sol.countSmaller(nums)
    print sol.countSmaller2(nums)
    print sol.countSmaller3(nums)
