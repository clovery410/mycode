class Solution(object):
    # This solution would exceed time limit
    def dp_solution(self, n):
        if n <= 0:
            return 0
        
        count = [0 for x in xrange(n+1)]
        count[0] = 0

        for i in xrange(1, n+1):
            curr_n = i
            curr_count = 0
            while curr_n > 0:
                d, curr_n = curr_n % 10, curr_n / 10
                if d == 1:
                    curr_count += 1
            count[i] = count[i-1] + curr_count

        return count[n]

    # Tricker solution, count appearance of 1 on each digit, from leetcode discussion
    def countDigitOne(self, n):
        if n <= 0:
            return 0
#        low, high = 0, n
        weight, count = 1, 0
        while n / weight > 0:
            low = n % weight
            high = n / (weight * 10)
            curr = (n / weight) % 10 
            if curr >= 2:
                count += (high + 1) * weight
            elif curr == 1:
                count += (low + 1) + high * weight
            else:
                count += high * weight
#            print weight, low, high, curr, count
            weight *= 10

        return count
    
if __name__ == '__main__':
    sol = Solution()
    n = 3184191
    n1 = 110
    print sol.dp_solution(n)
    print sol.countDigitOne(n)
