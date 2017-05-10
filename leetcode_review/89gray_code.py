class Solution(object):
    def grayCode(self, n):
        res = [0]
        for i in range(1, n+1):
            weight = pow(2, i-1)
            length = len(res)
            for j in reversed(range(length)):
                res.append(res[j] + weight)
        return res

if __name__ == "__main__":
    sol = Solution()
    print sol.grayCode(4)
