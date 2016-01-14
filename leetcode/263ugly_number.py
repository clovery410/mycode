class Solution(object):
    def isUgly(self, num):
        if num <= 0:
            return False
        
        while True:
            if num == 1:
                return True
            elif num % 2 == 0:
                num /= 2
            elif num % 3 == 0:
                num /= 3
            elif num % 5 == 0:
                num /= 5
            else:
                return False

if __name__ == '__main__':
    sol = Solution()
    print sol.isUgly(700)
