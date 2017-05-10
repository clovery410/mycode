class Solution(object):
    def isUgly(self, num):
        if num <= 0:
            return False
        while num != 1:
            temp = num
            if num % 2 == 0:
                num /= 2
            if num % 3 == 0:
                num /= 3
            if num % 5 == 0:
                num /= 5
            if num == temp:
                return False
        return True
            
