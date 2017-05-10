class Solution(object):
    #Solution1, brute-force, check one by one, running time is O(n^3)
    def longestPalindrome(self, s):
        n = len(s)
        curr = 0
        optimal = (0, 0)
        for i in xrange(n):
            for j in xrange(n):
                head, tail = i, j
                while head <= tail:
                    if s[head] != s[tail]:
                        break
                    else:
                        head += 1
                        tail -= 1
                if head > tail and (j - i) > curr:
                    curr = j - i
                    optimal = (i, j)

        return s[optimal[0]:optimal[1]+1]

    #Solution2, dp, use a table to record whether s[i:j] is a palindrome, time complexity is O(n^2), space complexity is also O(n^2)
    def longestPalindrome2(self, s):
        n = len(s)
        table = [[False for x in xrange(n)] for x in xrange(n)]
        #Initialize
        start = 0
        maxLength = 1
        for i in xrange(n):
            table[i][i] = True
        for i in xrange(n-1):
            if s[i+1] == s[i]:
                start = i
                maxLength = 2
                table[i][i+1] = True
        for d in xrange(3, n):
            for i in xrange(n-d+1):
                j = i + d - 1
                if s[i] == s[j] and table[i+1][j-1]:
                    table[i][j] = True
                    if d > maxLength:
                        maxLength = d
                        start = i
        return s[start:start+maxLength]

    #Solution3, continue to improve... traverse with the middle character, two conditions
    def longestPalindrome3(self, s):
        def checkPalindrome(lo, hi):
            res = 0
            while lo >= 0 and hi < len(s):
                if s[lo] == s[hi]:
                    res += 2
                    lo -= 1
                    hi += 1
                else:
                    break
            return res
        max_length = 0
        start = 0
        for mid in xrange(len(s)):
            odd_length = 1 + checkPalindrome(mid-1, mid+1)
            even_length = checkPalindrome(mid, mid+1)
            if max(odd_length, even_length) > max_length:
                if odd_length > even_length:
                    max_length = odd_length
                    start = mid - odd_length / 2
                else:
                    max_length = even_length
                    start = mid - even_length / 2
        return s[start: start + max_length]

    #soltution4, another dp, still TLE
    def longestPalindrome4(self, s):
        n = len(s)
        if n <= 1: return s

        dp = [[False for _ in xrange(n)] for _ in xrange(n)]
        max_len = start = end = 0

        for i in xrange(n):
            for j in xrange(i+1):
                if s[j] == s[i] and (j + 1 > i - 1 or dp[j+1][i-1]):
                    dp[j][i] = True
                    if i - j + 1 > max_len:
                        max_len = i - j + 1
                        start, end = j, i
        print max_len
        return s[start:end+1]

    #solution5, when you increase s by 1 character, you could only increase maxPalindromeLen by 1 or 2, and that new maxPalindrome includes this new character.
    def longestPalindrome5(self, s):
        n = len(s)
        if n <= 1: return s

        max_len, start = 1, 0
        for i in xrange(n):
            # check whether can expand palindrome by 2
            if i - max_len >= 1 and s[i-max_len-1:i+1] == s[i-max_len-1:i+1][::-1]:
                max_len += 2
                start = i - max_len + 1
                continue
            # check whether can expand palindrome by 1
            if i - max_len >= 0 and s[i-max_len:i+1] == s[i-max_len:i+1][::-1]:
                max_len += 1
                start = i - max_len + 1
        return s[start:start+max_len]
                
        
if __name__ =="__main__":
    s = "aaaaa"
    sol = Solution()
    print sol.longestPalindrome3(s)
    print sol.longestPalindrome4(s)
    print sol.longestPalindrome5(s)
