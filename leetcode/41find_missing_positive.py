from heapq import *
class Solution(object):
    #solution1, use heap to do it, but the running time here is not O(n) since the whole while loop is O(n), and inseide while, each heappop will consume O(log n), so the total running time will be O(nlogn)
    def firstMissingPositive(self, nums):
        heapify(nums)
        res = 1
        while len(nums) > 0:
            cur = heappop(nums)
            if cur > res:
                return res
            if cur == res:
                res = res + 1
        return res

    #solution2, use swapping to do it in linear time, learned from discuss
    def firstMissingPositive2(self, nums):
        n = len(nums)
        i = 0
        while i < n:
            if 0 < nums[i] <= n and nums[i] != i + 1:
                if nums[i] == nums[nums[i]-1]:
                    i += 1
                else:
                    temp = nums[i]
                    nums[i] = nums[nums[i]-1]
                    nums[temp-1] = temp
            else:
                i += 1
        i = 0
        while i < n and nums[i] == i + 1:
            i += 1
        return i + 1
        

if __name__ == "__main__":
    sol = Solution()
    print sol.firstMissingPositive([3,4,-1,1,2])
    print sol.firstMissingPositive2([3,4,-1,1,2])
