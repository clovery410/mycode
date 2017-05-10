import collections
class Solution(object):
    def longestSubstring(self, s, k):
        def helper(start, end):
            if end - start < k:
                return 0
            
            counter = collections.defaultdict(int)
            for i in xrange(start, end):
                counter[s[i]] += 1

            for mid in xrange(start, end):
                c = s[mid]
                if counter[c] < k:
                    return max(helper(start, mid), helper(mid+1, end))
            
            return end - start
        
        s = list(s)
        return helper(0, len(s))
    
    # solution2, learned from Stefan
    def longestSubstring2(self, s, k):
        if len(s) < k:
            return 0
        c = min(set(s), key = s.count)
        if s.count(c) >= k:
            return len(s)
        return max(self.longestSubstring2(x, k) for x in s.split(c))
        
            
if __name__ == "__main__":
    sol = Solution()
    s = "baaabcb"
    print sol.longestSubstring(s, 3)
    print sol.longestSubstring2(s, 3)
