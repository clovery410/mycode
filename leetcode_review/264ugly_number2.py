from heapq import *
class Solution(object):
    def nthUglyNumber(self, n):
        res = [1]
        heap = [(2, 2, 0), (3, 3, 0), (5, 5, 0)]
        heapify(heap)
        while len(res) < n:
            cur_num, cur_base, cur_idx = heappop(heap)
            res.append(cur_num)
            heappush(heap, (cur_base * res[cur_idx+1], cur_base, cur_idx+1))
            while heap[0][0] == cur_num:
                temp_num, temp_base, temp_idx = heappop(heap)
                heappush(heap, (temp_base * res[temp_idx+1], temp_base, temp_idx+1))
        return res[-1]

    # solution2, just use three pointers, not using heap
    def nthUglyNumber2(self, n):
        res = [1]
        idx2 = idx3 = idx5 = 0
        num2 = num3 = num5 = 1
        while len(res) < n:
            cur_num = min(num2 * 2, num3 * 3, num5 * 5)
            res.append(cur_num)
            if num2 * 2 == cur_num:
                idx2 += 1
                num2 = res[idx2]
            if num3 * 3 == cur_num:
                idx3 += 1
                num3 = res[idx3]
            if num5 * 5 == cur_num:
                idx5 += 1
                num5 = res[idx5]
        return res[-1]
    
if __name__ == "__main__":
    sol = Solution()
    print sol.nthUglyNumber(10)
    print sol.nthUglyNumber2(10)
