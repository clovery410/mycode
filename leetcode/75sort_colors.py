class Solution(object):
    #solution1, straight forward way of two-pass counting sort algorithm, count the total numbers of 0, 1, 2, then overwrite
    def sortColors(self, nums):
        red_count = white_count = blue_count = 0
        for num in nums:
            if num == 0:
                red_count += 1
            if num == 1:
                white_count += 1
            if num == 2:
                blue_count += 1
        for i in xrange(len(nums)):
            if red_count > 0:
                nums[i] = 0
                red_count -= 1
            elif white_count > 0:
                nums[i] = 1
                white_count -= 1
            elif blue_count > 0:
                nums[i] = 2
                blue_count -= 1
        return nums

    #solution2, follow-up, do it in one-pass, use three pointers
    def sortColors2(self, nums):
        def advancePointer(idx, val):
            if val == 0:
                while idx < len(nums) and nums[idx] == 0:
                    idx += 1
                return idx
            else:
                while idx >= 0 and nums[idx] == val:
                    idx -= 1
                return idx
                    
        idx0 = 0
        idx1 = idx2 = len(nums) - 1
        while idx0 <= idx1 and idx0 <= idx2:
            idx0 = advancePointer(idx0, 0)
            idx2 = advancePointer(idx2, 2)
            idx1 = advancePointer(idx2, 1)
            if idx0 > idx1 or idx0 > idx2 or idx1 < 0 or idx2 < 0:
                break
            if nums[idx0] == 2:
                nums[idx0], nums[idx2] = nums[idx2], nums[idx0]
            if nums[idx0] == 1:
                nums[idx0], nums[idx1] = nums[idx1], nums[idx0]
            if nums[idx1] == 2 and nums[idx2] == 1:
                nums[idx1], nums[idx2] = nums[idx2], nums[idx1]

        return nums

    #solution3, solution2 is too complicated, try with 3 way partition
    def sortColors3(self, nums):
        i = j = k = 0
        for j in xrange(len(nums)):
            if nums[j] == 1:
                if k < j:
                    nums[k], nums[j] = nums[j], nums[k]
                k += 1
            elif nums[j] == 0:
                nums[k], nums[j] = nums[j], nums[k]
                nums[i], nums[k] = nums[k], nums[i]
                i += 1
                k += 1
                    
            # if nums[j] != 2:
            #     nums[j], nums[k] = nums[k], nums[j]
            #     if nums[k] == 0:
            #         nums[i], nums[k] = nums[k], nums[i]
            #         i += 1
            #     k += 1

        return nums
                

if __name__ == "__main__":
    sol = Solution()
    nums = [2, 0, 1]
    print nums
    print sol.sortColors2(nums)
    print sol.sortColors3(nums)
