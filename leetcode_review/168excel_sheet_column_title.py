class Solution(object):
    def convertToTitle(self, n):
        def getNext(n):
            if n < 0:
                return ''
            cur_num = n % 26
            cur_char = chr(ord('A') + cur_num)
            return getNext(n / 26 - 1) + cur_char

        return getNext(n - 1)
        
if __name__ == "__main__":
    sol = Solution()
    print sol.convertToTitle(77)
