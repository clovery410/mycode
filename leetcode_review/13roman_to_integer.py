class Solution(object):
    def romanToInt(self, s):
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        l = len(s)
        if l == 0: return 0
        res = roman[s[-1]]
        if l > 1:
            for i in reversed(xrange(l-1)):
                if roman[s[i]] >= roman[s[i+1]]:
                    res += roman[s[i]]
                else:
                    res -= roman[s[i]]
        return res
