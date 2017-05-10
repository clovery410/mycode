class Solution(object):
    def fizzBuzz(self, n):
        res = []
        for i in xrange(1, n+1):
            if i % 3 != 0 and i % 5 != 0:
                c = str(i)
            else:
                c = ''
                if i % 3 == 0:
                    c += 'Fizz'
                if i % 5 == 0:
                    c += 'Buzz'
            res.append(c)
            
        return res

if __name__ == "__main__":
    sol = Solution()
    print sol.fizzBuzz(15)
