class Solution(object):
    def hanoi(self, n):
        def _hanoi(n, moveFrom, moveTo):
            if n == 1:
                print str(n) + ': ' + str(moveFrom) + ' -> ' + str(moveTo)
            else:
                moveTmp = 3 - moveFrom - moveTo
                _hanoi(n - 1, moveFrom, moveTmp)
                print str(n) + ': ' + str(moveFrom) + ' -> ' + str(moveTo)
                _hanoi(n - 1, moveTmp, moveTo)

        _hanoi(n, 0, 2)

if __name__ == '__main__':
    sol = Solution()
    sol.hanoi(3)
            
                
        
