class Solution(object):
    # solution1, recursive solution, but not right
    def canWinNim(self, n, cacahe = {}):
        if n <= 0:
            return False
        if n <= 3:
            return True

        if n in cache:
            return cache[n]
        res = False
        for i in xrange(1, 4):
            if not self.canWinNim(n - i):
                res = True
                break
        cache[n] = res
        return res

    # solution2, use math trick, since if you are fall into 4 stones, you will absolutely lose.. so just check whether the number is a multiple of 4
    def canWinNim2(self, n):
        if n % 4 == 0:
            return False
        return True
    

    
