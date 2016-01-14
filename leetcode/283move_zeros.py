class Solution(object):
    def moveZeroes(self, nums):
        n = len(nums)
        i = 0
        count = 0
        while count < n:
            if nums[i] == 0:
                zero = nums.pop(i)
                nums.append(zero)
            else:
                i += 1
            count += 1

        print nums


if __name__ == '__main__':
    nums = [0, 0, 1]
    sol = Solution()
    sol.moveZeroes(nums)
                
