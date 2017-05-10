from heapq import *
class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        res = [1]
        heap = []
        for prime in primes:
            heappush(heap, (prime, prime, 0))

        while len(res) < n:
            cur_num, cur_base, cur_idx = heappop(heap)
            res.append(cur_num)
            cur_idx += 1
            heappush(heap, (res[cur_idx] * cur_base, cur_base, cur_idx))
            while heap[0][0] == cur_num:
                temp_num, temp_base, temp_idx = heappop(heap)
                heappush(heap, (temp_base * res[temp_idx+1], temp_base, temp_idx+1))
        return res[-1]

    # solution2, easy version heap, but seems TLE
    def nthSuperUglyNumber2(self, n, primes):
        heap = [(1, 0)]
        for i in xrange(n):
            val, idx = heappop(heap)
            for j in xrange(idx, len(primes)):
                heappush(heap, (val * primes[j], j))
        return val

    # use k pointers
    def nthSuperUglyNumber3(self, n, primes):
        res = [1]
        factors = [x for x in primes]
        pointers = [0] * n
        while len(res) < n:
            next_num = min(factors)
            res.append(next_num)
            for i, factor in enumerate(factors):
                if factor == next_num:
                    pointers[i] += 1
                    factors[i] = primes[i] * res[pointers[i]]
        return res[-1]
            
