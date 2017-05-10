class Solution(object):
    # solution1, use dfs search, but MLE on Leetcode
    def lexicalOrder(self, n):
        def dfs(cur_num):
            if cur_num > n:
                return
            res.append(cur_num)
            cur_num *= 10
            for digit in range(10):
                if cur_num + digit > n:
                    break
                dfs(cur_num + digit)

        res = []
        for first_digit in xrange(1, 10):
            dfs(first_digit)
        return res

    # solution2, since above solution reach MLE, so do it iteratively instead of recursion
    def lexicalOrder2(self, n):
        current = 1
        res = []
        while True:
            res.append(current)
            if current * 10 <= n:
                current *= 10
            else:
                while current:
                    if current % 10 + 1 < 10 and current + 1 <= n:
                        current += 1
                        break
                    else:
                        current /= 10
                        
            if current == 0:
                break
            
        return res
        

if __name__ == "__main__":
    sol = Solution()
    print sol.lexicalOrder(49999)
    print sol.lexicalOrder2(49999)
