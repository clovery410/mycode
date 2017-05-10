import time
class Solution(object):
    #Solution1, brute-force, TLE
    def isScramble(self, s1, s2):
        if s1 == s2 or s1 == s2[::-1]:
            return True
        l = len(s1)
        if l <= 1:
            return False
        
        for i in range(1, l):
            if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]):
                return True
            if self.isScramble(s1[:i], s2[l-i:]) and self.isScramble(s1[i:], s2[:l-i]):
                return True
        return False

    #Solution2, optimize solution with memo
    def isScramble2(self, s1, s2):
        def _isScramble(s1, s2):
            if (s1, s2) in cache:
                return cache[(s1, s2)]
            l = len(s1)
            if l != len(s2) or sorted(s1) != sorted(s2): # adding this checking to pruning
                return False
            if s1 == s2 or s1 == s2[::-1]:
                return True
            elif l <= 1:
                return False
            for i in range(1, l):
                if _isScramble(s1[:i], s2[:i]) and _isScramble(s1[i:], s2[i:]):
                    cache[(s1, s2)] = True
                    return True
                if _isScramble(s1[:i], s2[l-i:]) and _isScramble(s1[i:], s2[:l-i]):
                    cache[(s1, s2)] = True
                    return True
            cache[(s1, s2)] = False
            return False
        cache = {}
        return _isScramble(s1, s2)

    #Solution3, dp, use a three-dimension array to store the state: match[size][index1][index2], size is the comparing size of two strings, index1 is the start index of string1, index2 is the start index of string2
    #time complexcity is O(n^4)
    def isScramble3(self, s1, s2):
        n = len(s1)
        if n != len(s2): return False
        if n == 0: return True
        if len(s1) == 1: return s1 == s2

        match = [[[False] * n for _ in xrange(n)] for _ in xrange(n+1)]
        for i in xrange(1, n+1): # length of current comparing string
            for j in xrange(n-i+1): # start index of substring1
                for k in xrange(n-i+1): # start index of substring2
                    if i == 1: match[i][j][k] = s1[j] == s2[k]
                    for m in xrange(1, i):
                        if match[m][j][k] and match[i-m][j+m][k+m]:
                            match[i][j][k] = True
                        elif match[m][j][k+i-m] and match[i-m][j+m][k]:
                            match[i][j][k] = True
        return match[n][0][0]
        
    
if __name__ == "__main__":
    s1 = "abcdefghijklmn"
    s2 = "efghijklmncadb"
    sol = Solution()
    time1 = time.time()
    print sol.isScramble(s1, s2)
    print "solution1 --- %s second ---" % (time.time() - time1)
    time2 = time.time()
    print sol.isScramble2(s1, s2)
    print "solution2 --- %s second ---" % (time.time() - time2)
    time3 = time.time()
    print sol.isScramble3(s1, s2)
    print "solution3 --- %s second ---" % (time.time() - time3)
