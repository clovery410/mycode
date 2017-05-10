class Solution(object):
    def increasingTriplet(self, nums):
        first = second = third = None
        for num in nums:
            if first == None or num <= first:
                first = num
            elif second == None or num <= second:
                second = num
            else:
                third = num
                
        return third != None

if __name__ == "__main__":
    sol = Solution()
    nums = [1,2,3,4,5]
    print sol.increasingTriplet(nums)
                
