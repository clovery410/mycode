from collections import deque
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        i = j = 0
        queue = deque(nums1[:m])
        
        while queue and j < n:
            if queue[0] < nums2[j]:
                nums1[i] = queue.popleft()
            else:
                nums1[i] = nums2[j]
                j += 1
            i += 1
            
        if j < n:
            while j < n:
                nums1[i]  = nums2[j]
                i += 1
                j += 1
        elif queue:
            while queue:
                nums1[i] = queue.popleft()
                i += 1


    # This algorithm works really good! implement from the end of the array, learnt from Leetcode forum
    def simple_solution(self, nums1, m, nums2, n):
        for i in reversed(xrange(m+n)):
            if m != 0 and (n == 0 or nums1[m-1] > nums2[n-1]):
                m -= 1
                nums1[i] = nums1[m]
            else:
                n -= 1
                nums1[i] = nums2[n]

if __name__ == '__main__':
    sol = Solution()
    nums1 = [2,3,4,5]
    nums2 = [0,1,6,7]
    m = n = 2

    sol.simple_solution(nums1, m, nums2, n)
    print nums1
