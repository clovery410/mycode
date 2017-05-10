class Solution(object):
    def nextPermutation(self, nums):
        def reversePart(start):
            end = len(nums) - 1
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        i = len(nums) - 2
        while i >= 0:
            if nums[i] < nums[i+1]:
                j = len(nums) - 1
                while j >= i:
                    if nums[j] > nums[i]:
                        nums[i], nums[j] = nums[j], nums[i]
                        break
                    j -= 1
                break
            i -= 1
        reversePart(i+1)

    #solution2, more clear logic, and faster performance
    def nextPermutation2(self, nums):
        def reversePart(start):
            end = len(nums) - 1
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1

        # if i >= 0, find, first element who is greater than nums[i] from back, and switch them
        if i >= 0:
            j = len(nums) - 1
            while j > i:
                if nums[j] > nums[i]:
                    nums[i], nums[j] = nums[j], nums[i]
                    break
                j -= 1
        reversePart(i+1)
            
        
