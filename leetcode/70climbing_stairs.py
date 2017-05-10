class Solution(object):
    def climbStairs(self, n):
        if n <= 2:
            return n
        step_one, step_two = 2, 1
        
        for i in xrange(2, n):
            curr = step_one + step_two
            step_one, step_two = curr, step_one
        return curr

    def dp_solution(self, n):
        if n <= 2:
            return n
        record = [0 for x in xrange(n)]
        record[0], record[1] = 1, 2

        for i in xrange(2, n):
            record[i] = record[i-1] + record[i-2]
        return record[-1]

    
