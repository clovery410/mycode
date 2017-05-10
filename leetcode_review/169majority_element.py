class Solution(object):
    def majorityElement(self, nums):
        count, candidate = 0, nums[0]
        for num in nums:
            if count == 0:
                candidate = num
                count += 1
            else:
                if num == candidate:
                    count += 1
                else:
                    count -= 1
        return candidate

if __name__ == "__main__":
    nums = [1, 1, 1, 2, 3]
    sol = Solution()
    print sol.majorityElement(nums)
