class Solution(object):
    #Solution1, brute-force recursive solution
    def maxEnvelopes(self, envelopes):
        def helper(last_pair, max_num, idx):
            if idx >= len(envelopes):
                return max_num
            curr_l, curr_h = envelopes[idx][0], envelopes[idx][1]
            if curr_l > last_pair[0] and curr_h > last_pair[1]:
                return max(helper(last_pair, max_num, idx+1), helper((curr_l, curr_h), max_num + 1, idx+1))
            else:
                return helper(last_pair, max_num, idx+1)
            
        envelopes = sorted(envelopes, key = lambda x: (x[0], x[1]))
        return helper((0, 0), 0, 0)

    #Solution2, dp solution, running time is O(n^2), but still TLE
    def maxEnvelopes2(self, envelopes):
        envelopes = sorted(envelopes, key = lambda x: (x[0], x[1]))
        dp = [1] * len(envelopes)
        ret = 1
        for i in xrange(1, len(envelopes)):
            for j in xrange(i):
                if envelopes[i][0] > envelopes[j][0] and envelopes[i][1] > envelopes[j][1]:
                    dp[i] = max(dp[i], dp[j] + 1)
            ret = max(ret, dp[i])
        return ret

    #Solution3, use binary search to optimize, running time is O(nlogn)
    def maxEnvelopes3(self, envelopes):
        envelopes = sorted(envelopes, key = lambda x: (x[0], -x[1]))
        lis = []
        for envelope in envelopes:
            if len(lis) == 0 or envelope[1] > lis[-1]:
                lis.append(envelope[1])
            else:
                idx = self.binarySearch(lis, envelope[1])
                lis[idx] = envelope[1]
        return len(lis)

    def binarySearch(self, nums, val):
        s, e = 0, len(nums)
        while s <= e:
            mid = (e - s) / 2 + s
            if nums[mid] < val:
                s = mid + 1
            else:
                e = mid - 1
        return s

if __name__ == "__main__":
    envelopes = [[5,4], [6,4], [6,7], [2,3]]
    sol = Solution()
    print sol.maxEnvelopes(envelopes)
    print sol.maxEnvelopes2(envelopes)
    print sol.maxEnvelopes3(envelopes)
