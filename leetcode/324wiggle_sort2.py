class Solution(object):
    def partition_into3(self, p_i, nums):
        n = len(nums)
        p = nums[p_i]
        nums[0], nums[p_i] = nums[p_i], nums[0]

        i = k = 0
        for j in xrange(n):
            if nums[j] == p:
                if i != j:
                    nums[i], nums[j] = nums[j], nums[i]
                i += 1
            if nums[j] < p:
                nums[j], nums[i] = nums[i], nums[j]
                nums[k], nums[i] = nums[i], nums[k]
                i += 1
                k += 1

        return k, i-1

    def partition_for_median(self, nums):
        length = len(nums)
        median = length / 2
        start, end = self.partition_into3(0, nums)
        while True:
            if start <= median and median <= end:
                print nums
                return median
            elif start > median:
                start, end = self.partition_into3(start-1, nums)
            else:
                start, end = self.partition_into3(end+1, nums)
        
    
    def wiggleSort(self, nums):
        median = self.partition_for_median(nums)
        l = len(nums)
        ans = []
        j = l-1
        if l % 2 == 0:
            i = median-1
            while j > median-1:
                ans.append(nums[i])
                ans.append(nums[j])
                i -= 1
                j -= 1
        else:
            i = median
            while j > median:
                ans.append(nums[i])
                ans.append(nums[j])
                i -= 1
                j -= 1
            ans.append(nums[0])

        return ans
    
if __name__ == '__main__':
    nums = [1,3,2,2,2,1,1,3,1,2,3]
    nums2 = [4, 5, 5, 6]
    sol = Solution()
#    print sol.partition_for_median(nums)
#    print sol.partition_into3(2, nums)
    print sol.wiggleSort(nums2)
    
