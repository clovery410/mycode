class Solution(object):
    def romanToInt(self, s):
        d = {}
        d['I'] = 1
        d['V'] = 5
        d['X'] = 10
        d['L'] = 50
        d['C'] = 100
        d['D'] = 500
        d['M'] = 1000
        n = len(s)
        val = 0
        i = 0

        while i < n - 1:
            if s[i] == 'I' and (s[i+1] == 'V' or s[i+1] == 'X'):
                val += d[s[i+1]] - 1
                i += 2
            elif s[i] == 'X' and (s[i+1] == 'L' or s[i+1] == 'C'):
                val += d[s[i+1]] - 10
                i += 2
            elif s[i] == 'C' and (s[i+1] == 'D' or s[i+1] == 'M'):
                val += d[s[i+1]] - 100
                i += 2
            else:
                val += d[s[i]]
                i += 1
        if i == n - 1:
            val += d[s[i]]

        return val

    def shortSolution(self, s):
        d = {}
        d['I'] = 1
        d['V'] = 5
        d['X'] = 10
        d['L'] = 50
        d['C'] = 100
        d['D'] = 500
        d['M'] = 1000
        n = len(s)
        val = 0
        prev = 1000
        for i in xrange(n):
            curr = d[s[i]]
            if curr > prev:
                val += curr - 2 * prev
            else:
                val += curr
            prev = curr
        return val

if __name__ == '__main__':
    roman = "LXXIX"
    sol = Solution()
    print sol.romanToInt(roman)
    print sol.shortSolution(roman)
