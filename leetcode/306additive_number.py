class Solution(object):
    def isAdditiveNumber(self, num):
        def findNext(idx, pre, cur):
            if idx >= len(num): return True
            if num[idx] == '0':
                return findNext(idx+1, cur, 0)

            for end in range(idx, len(num)):
                if pre + cur == int(num[idx:end+1]):
                    if findNext(end+1, cur, int(num[idx:end+1])):
                        return True
            return False

        if len(num) <= 2: return False
        
        if num[0] == '0':
            if num[1] == '0': return findNext(2, 0, 0)
            else:
                for j in range(1, len(num)-1):
                    if findNext(j+1, 0, int(num[1:j+1])): return True
                return False
        else:
            for i in range(len(num)-1):
                pre = int(num[:i+1])
                if num[i+1] == '0':
                    if findNext(i+2, pre, 0): return True
                else:
                    for j in range(i+1, len(num)-1):
                        cur = int(num[i+1:j+1])
                        if findNext(j+1, pre, cur): return True
            return False

if __name__ == "__main__":
    sol = Solution()
    print sol.isAdditiveNumber('0199100199')
                
