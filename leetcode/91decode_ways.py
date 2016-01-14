class Solution(object):
    def __init__(self):
        self.ans = 1
        self.valid = True
    
    def count(self, string):
        if len(string) >= 2 and string[0] >= '3' and string[1] == '0':
            self.valid = False
        if len(string) <= 1:
            return
        if (string[0] == '0'):
            self.ans -= 1
        elif (string[0] == '1' or string[0] == '2') and string[1] == '0':
            self.count(string[2:])
        elif string[0] == '1' and string[1] != '0':
            self.ans += 1
            self.count(string[1:])
            self.count(string[2:])
        elif string[0] == '2' and string[1] <= '6' and string[1] != '0':
            self.ans += 1
            self.count(string[1:])
            self.count(string[2:])
        else:
            self.count(string[1:])

    def numDecodings(self, s):
        if len(s) > 0:
            self.count(s)

        if self.valid:
            return self.ans

        return 0

    def dp_solution(self, s):
        if len(s) <= 0 or s[0] == '0':
            return 0
        elif len(s) == 1:
            return 1
        elif s[0] > '2' and s[1] == '0':
            return 0
        ways = [1 for x in xrange(len(s))]
        if (s[0] == '1' and s[1] != '0') or (s[0] == '2' and s[1] != '0' and s[1] < '7'):
            ways[1] = 2
        else:
            ways[1] = 1
        for i in xrange(2, len(s)):
            if s[i] == '0' and (s[i-1] == '0' or s[i-1] > '2'):
                return 0
            if s[i] == '0':
                ways[i] = ways[i-2]
            elif s[i] != '0' and (s[i-1] == '1' or (s[i-1] == '2' and s[i] <= '6')):
                ways[i] = ways[i-2] + ways[i-1]
            else:
                ways[i] = ways[i-1]
        print ways
        return ways[-1]
    
if __name__ == '__main__':
    s = "301"
    s2 = "4757562545844617494555774581341211511296816786586787755257741178599337186486723247528324612117156948"
    sol = Solution()
    print sol.numDecodings(s)
    print sol.dp_solution(s)
