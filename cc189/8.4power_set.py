class Solution(object):
    #Solution1, recursive solution
    def powerSet(self, s):
        if len(s) == 0:
            return [[]]
        else:
            res = self.powerSet(s[:-1])
            length = len(res)
            for i in xrange(length):
                res.append(res[i] + [s[-1],])
            return res

    #Solution2, make use of combinatorics, since for each number, we can either choose or not choose, so that we would have 2^n possible subsets.
    #If each choosing can be treated as 1 and each not choosing can be treated as 0, then each subset can be represented as a bianry stirng.
    #Generating all subsets, just come down to generating all binary numbers, we iterate through all numbers from 0 to 2^n and translate each binary representation into a set.
    def powerSet2(self, s):
        def translateIntoSet(num):
            subset = []
            index = 0
            while num > 0:
                if num & 1:
                    subset.append(s[index])
                num = num >> 1
                index += 1
            return subset
        res = []
        for i in xrange(1 << len(s)):
            res.append(translateIntoSet(i))
        return res
            
if __name__ == "__main__":
    sol = Solution()
    s = [1, 2, 3]
    print sol.powerSet2(s)

        
        
