import collections
class Solution(object):
    # base question
    def isSubsequence(self, s, t):
        if len(s) == 0:
            return True
        
        s_i, t_i = 0, 0
        while t_i < len(t):
            if s[s_i] == t[t_i]:
                s_i += 1
            if s_i == len(s):
                return True
            t_i += 1
        return False

    # follow up solution: what if there are lots of incoming S. We can pre-store the index information
    def isSubsequence2(self, s, t):
        def binarySearch(nums, idx):
            s, e = 0, len(nums) - 1
            while s <= e:
                mid = (e - s) / 2 + s
                if nums[mid] > idx:
                    e = mid - 1
                else:
                    s = mid + 1
            return nums[s]
        
        indices = collections.defaultdict(list)
        for i, c in enumerate(t):
            indices[c].append(i)

        cur_idx = -1
        for c in s:
            if c not in indices or indices[c][-1] <= cur_idx:
                return False
            cur_idx = binarySearch(indices[c], cur_idx)
        return True
            

if __name__ == "__main__":
    sol = Solution()
    s = "acb"
    t = "ahbgdc"
    print sol.isSubsequence(s, t)
    print sol.isSubsequence2(s, t)
