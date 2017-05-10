import heapq
class Solution(object):
    #Solution1, use heap
    def nthSuperUglyNumber(self, n, primes):
        heap = [(1, 0)]
        for i in xrange(n):
            val, idx = heapq.heappop(heap)
            for j in xrange(idx, len(primes)):
                heapq.heappush(heap, (val * primes[j], j))
        return val

    #solution2, use k pointers (k is all prime numbers)
    def nthSuperUglyNumber2(self, n, primes):
        ugly = [1] * n
        pointers = [0] * len(primes)
        factors = primes[:]
        for i in xrange(1, n):
            ugly[i] = min(factor for factor in factors)
            for j in xrange(len(factors)):
                if ugly[i] == factors[j]:
                    pointers[j] += 1
                    factors[j] = ugly[pointers[j]] * primes[j]
        return ugly[-1]

    #solution3,
    def nthSuperUglyNumber3(self, n, primes):
        heap = [(p, 0, p) for p in primes]
        uglyNum = [1] * n
        heapq.heapify(heap)
        for i in xrange(1, n):
            num, idx, p = heap[0]
            uglyNum[i] = num
            while len(heap) > 0 and heap[0][0] == num:
                _num, _idx, _p = heapq.heappop(heap)
                heapq.heappush(heap, (uglyNum[_idx] * _p, _idx + 1, _p))
        return uglyNum[-1]

if __name__ == "__main__":
    sol = Solution()
    primes = [2,3,5,7,11,13]
    print sol.nthSuperUglyNumber2(10, primes)
    print sol.nthSuperUglyNumber3(10, primes)
