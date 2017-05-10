import heapq
class Solution(object):
    #Solution1, but TLE
    def nthUglyNumber(self, n):
        dp = {1}
        cur = 2
        while len(dp) < n:
            for num in [2, 3, 5]:
                if cur % num == 0 and cur / num in dp:
                    dp |= {cur}
            cur += 1
        return max(dp)

    #Solution2, using heap, still really slow, need improve further
    def nthUglyNumber2(self, n):
        heap = [1]
        pre, count = 0,  1
        while count <= n:
            cur = heapq.heappop(heap)
            if cur != pre:
                for num in [2, 3, 5]:
                    heapq.heappush(heap, cur * num)
                count += 1
            pre = cur
        return pre

    #Solution3, using heap, similar idea as solution2, but optimized the duplicate condition, not push the duplicate numbers into heap by including a second variable fact which denote the previous factor it used. Since if we extract (2, 3) from heap, there is no need to multiply it by 2 again, (2, 2) will cover that number
    def nthUglyNumber3(self, n):
        heap = [(1, 1)]
        for i in range(n):
            val, fact = heapq.heappop(heap)
            for num in 2, 3, 5:
                if num >= fact:
                    heapq.heappush(heap, (val * num, num))
        return val

    #Solution4, three pointers solution
    def nthUglyNumber4(self, n):
        ugly = [1] * n
        t2 = t3 = t5 = 0
        for i in range(1, n):
            ugly[i] = min(ugly[t2] * 2, ugly[t3] * 3, ugly[t5] * 5)
            if ugly[i] == ugly[t2] * 2: t2 += 1
            if ugly[i] == ugly[t3] * 3: t3 += 1
            if ugly[i] == ugly[t5] * 5: t5 += 1
        return ugly[-1]

if __name__ == "__main__":
    sol = Solution()
    print sol.nthUglyNumber(284)
    print sol.nthUglyNumber2(284)
    print sol.nthUglyNumber3(284)
    print sol.nthUglyNumber4(284)
