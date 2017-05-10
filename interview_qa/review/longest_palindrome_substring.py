cur_max = 0
res_idx = [0, 0]

def longestSubstring(s):

    def getPalindrome(mid1, mid2):
        while mid1 >= 0 and mid2 < len(s) and s[mid1] == s[mid2]:
            mid1 -= 1
            mid2 += 1
        return (mid1 + 1, mid2 - 1)

    def updateResult(start, end):
        global cur_max
        global res_idx
        if end - start + 1 > cur_max:
            cur_max = end - start + 1
            res_idx = [start, end]
        return res_idx

    for mid in xrange(len(s)):
        start, end = getPalindrome(mid, mid)
        res_idx = updateResult(start, end)
        if mid < len(s) - 1:
            start, end = getPalindrome(mid, mid + 1)
            res_idx = updateResult(start, end)
    return res_idx

print longestSubstring('aabbdb')
    
            
