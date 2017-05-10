import collections
class Solution(object):
    # solution1, not optimal solution, which in worst cast running time is O(n^2)
    def lengthOfLongestSubstringTwoDistinct(self, s):
        if len(s) <= 2:
            return len(s)

        max_len = 1
        cur_len = 1
        for i in xrange(1, len(s)):
            if s[i] != s[i-1]:
                pre, cur = s[i-1], s[i]
                j = i - 1
                while j >= 0 and (s[j] == pre or s[j] == cur):
                    j -= 1
                cur_len = i - j
            else:
                cur_len += 1
            max_len = max(max_len, cur_len)
            
        return max_len

    # solution2, using sliding window, maintain a current window with maximum size of two, whenever window size exceeds two, remove the minimun value one, and update the starting index. Running time is O(n)
    def lengthOfLongestSubstringTwoDistinct2(self, s):
        if len(s) <= 2:
            return len(s)
        max_len = 0
        start_idx = 0
        window = collections.defaultdict(int)
        
        for i, c in enumerate(s):
            window[c] = i

            if len(window) > 2:
                rm_idx, rm_char = min([(idx, char) for char, idx in window.items()])
                del window[rm_char]
                start_idx = rm_idx + 1
                
            max_len = max(max_len, i - start_idx + 1)
            
        return max_len

if __name__ == "__main__":
    sol = Solution()
    print sol.lengthOfLongestSubstringTwoDistinct("eebeeeaee")
    print sol.lengthOfLongestSubstringTwoDistinct2("eebeeaeee")
