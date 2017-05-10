class Solution(object):
    # learned from discuss, with the attribute that:
    # ab % k = (a%k) * (b%k) % k => a ^ 1234567 % k = (a ^ 1234560 % k) * (a ^ 7 % k) % k
    # so if we name f(a, b) = a ^ b % k,
    # then f(a, 1234567)
    #      = f(a, 1234560) * f(a, 7) % k
    #      = f(f(a, 123456), 10) * f(a, 7) % k
    
    def superPow(self, a, b):
        def powMod(a, k):
            res = 1
            a %= base
            for i in xrange(k):
                res = (a * res) % base
            return res
        
        if len(b) == 0:
            return 1
        base = 1337
        last_digit = b.pop()
        return powMod(self.superPow(a, b), 10) * powMod(a, last_digit) % base

if __name__ == "__main__":
    sol = Solution()
    print sol.superPow(2, [3,1])
