class Solution(object):
    #solution1, O(n) time, O(n) space
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        
        chars = collections.defaultdict(int)
        for c in s:
            chars[c] += 1
        for c in t:
            chars[c] -= 1
            if chars[c] < 0:
                return False

        return True

    #solution2, O(n logn) time, O(1) space
    def isAnagram2(self, s, t):
        if len(s) != len(t):
            return False
        
        s_lst = sorted(list(s))
        t_lst = sorted(list(t))
        for i in xrange(len(s_lst)):
            if s_lst[i] != t_lst[i]:
                return False
        return True
