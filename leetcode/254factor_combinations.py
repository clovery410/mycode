import time, math
class Solution(object):
    #solution1, too slow, hit TLE
    def getFactors(self, n):
        def generate(start, remain, cur_sol, all_sols):
            if remain == 1:
                if len(cur_sol) > 1:
                    all_sols.append(list(cur_sol))
                return
            for i in xrange(start, remain + 1):
                if remain % i == 0:
                    cur_sol.append(i)
                    generate(i, remain / i, cur_sol, all_sols)
                    cur_sol.pop()

        res = []
        generate(2, n, [], res)
        return res

    #solution2, try to construct the factor array first, but this one memory limit exceed
    def getFactors2(self, n):
        def generate(start, remain, cur_sol, all_sols):
            if remain == 1:
                all_sols.append(list(cur_sol))
                return
            for i in xrange(start, len(factors)):
                cur_num = factors[i]
                if remain % cur_num == 0:
                    cur_sol.append(cur_num)
                    generate(i, remain / cur_num, cur_sol, all_sols)
                    cur_sol.pop()

        factors = [item for item in range(2, n) if n % item == 0]
        print factors
        res = []
        generate(0, n, [], res)
        return res

    #solution3, try to use sqrt to import time complexcity
    def getFactors3(self, n):
        def generate(remain):
            res = []
            for i in xrange(2, int(math.sqrt(remain)) + 1):
                if remain % i == 0:
                    middle = generate(remain / i)
                    res += [[i, remain / i]] + [[i] + x for x in middle if x[0] >= i]
            return res
        return generate(n)
    
    #solution4, more concise version of solution3 using list comprehension
    def getFactors4(self, n):
        res = []
        for i in xrange(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                res += [[i, n / i]] + [[i] + x for x in self.getFactors4(n / i) if x[0] >= i]
        return res
                     

if __name__ == "__main__":
    sol = Solution()
    time1 = time.time()
    print sol.getFactors(23848713)
    print "solution1 --- %s second ---" % (time.time() - time1)
    time2 = time.time()
    print sol.getFactors2(23848713)
    print "solution2 --- %s second ---" % (time.time() - time2)
    time3 = time.time()
    print sol.getFactors3(23848713)
    print "solution3 --- %s second ---" % (time.time() - time3)
                    
