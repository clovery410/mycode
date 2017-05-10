class Solution(object):
    def isHappy(self, n):
        visited = set()
        while True:
            if n == 1:
                return True
            if n in visited:
                return False
            visited.add(n)
            tmp = 0
            while n:
                cur_digit = n % 10
                n /= 10
                tmp += cur_digit ** 2
            n = tmp
