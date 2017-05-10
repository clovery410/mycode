class Solution(object):
    def jump(self, nums):
        l = len(nums)
        count, idx = 0, 0
        while idx < l:
            if idx == l - 1:
                return count
            count += 1
            cur_total, num = 0, nums[idx]
            for step in range(1, num+1):
                if idx + step >= l - 1:
                    return count
                if nums[idx+step] + step >= cur_total:
                    cur_total = nums[idx+step] + step
                    new_idx = idx + step
            idx = new_idx

    #solution2, learned from discuss
    def jump2(self, nums):
        end, count = 0, 0
        cur_max = 0
        for i in xrange(len(nums)-1):
            cur_max = max(cur_max, nums[i] + i)
            if i == end:
                count += 1
                end = cur_max
        return count

    #solution3, also learned from discuss, which is for python
    """
    Suppose we devided the arrays into segments depending on the element in the array. 
    So for each segment, we find the farest index we can jump. 
    For exampe, the first segment is always A[0]. 
    The second will be from A[1] for A[A[0]]. 
    The third will be from A[A[0]] to the farthest index we can find in the second segment. 
    We start looking between the end of the last segment and the begin of the next segment.
    """
    def jump3(self, nums):
        count = lastIdx = nextIdx = 0
        while nextIdx < len(nums) - 1:
            count += 1
            lastIdx, nextIdx = nextIdx, max(nums[x] + x for x in xrange(lastIdx, nextIdx+1))
        return count

if __name__ == "__main__":
    sol = Solution()
    print sol.jump([5,3,1,1,2,1,4,2,1,3,1])
    print sol.jump2([5,3,1,1,2,1,4,2,1,3,1])
    print sol.jump3([5,3,1,1,2,1,4,2,1,3,1])
