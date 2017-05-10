class Solution(object):
    #Solution1, brute-force, recursive, TLE
    def maxNumber(self, nums1, nums2, k):
        def helper(m, n, idx1, idx2, num, count):
            if m - idx1 + n - idx2 < count:
                cache[(idx1, idx2, count)] = 0
                return 0
            if count == 0:
                if num > self.max_val:
                    self.max_val = num
                cache[(idx1, idx2, count)] = num
                return num
            v1 = v2 = v3 = v4 = 0
            if idx1 < m:
                v1 = helper(m, n, idx1+1, idx2, num, count)
                v2 = helper(m, n, idx1+1, idx2, num * 10 + nums1[idx1], count-1)
            if idx2 < n:
                v3 = helper(m, n, idx1, idx2+1, num, count)
                v4 = helper(m, n, idx1, idx2+1, num * 10 + nums2[idx2], count-1)
            cache[(idx1, idx2, count)] = max(v1, v2, v3, v4)
            return cache[(idx1, idx2, count)]

        self.max_val = 0
        cache = {}
        helper(len(nums1), len(nums2), 0, 0, 0, k)
        return [int(x) for x in str(self.max_val)]

    #Solution2
    def maxNumber2(self, nums1, nums2, k):
        _max = [0] * k
        for i in range(max(0, k-len(nums2)), min(k, len(nums1)) + 1):
            cur_max = self.merge(self.getSubMax(nums1, i), self.getSubMax(nums2, k-i))
            if self.isGreater(cur_max, 0, _max, 0):
                _max = cur_max
        return _max
        
    def getSubMax(self, nums, k):
        res = [0] * k
        j, l = 0, len(nums)
        for i in range(l):
            while 0 < j and nums[i] > res[j-1] and k - j < l - i:
                j -= 1
            if j < k:
                res[j] = nums[i]
                j += 1
        return res

    def merge(self, nums1, nums2):
        res = [0] * (len(nums1) + len(nums2))
        p1 = p2 = 0
        for i in range(len(nums1) + len(nums2)):
            if self.isGreater(nums1, p1, nums2, p2):
                res[i] = nums1[p1]
                p1 += 1
            else:
                res[i] = nums2[p2]
                p2 += 1
        return res

    def isGreater(self, nums1, p1, nums2, p2):
        while p1 < len(nums1) and p2 < len(nums2) and nums1[p1] == nums2[p2]:
            p1 += 1
            p2 += 1
        return p2 == len(nums2) or p1 < len(nums1) and nums1[p1] > nums2[p2]
            
if __name__ == "__main__":
    nums1 = [6,7]
    nums2 = [6,0,4]
    sol = Solution()
    print sol.maxNumber2(nums1, nums2, 5)
    # print sol.getSubMax(nums2, 2)
