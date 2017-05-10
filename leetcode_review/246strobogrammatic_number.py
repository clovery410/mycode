class Solution(object):
    #solution1, recursive solution
    def isStrobogrammatic(self, num):
        strobo = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
        if len(num) == 0:
            return True
        if len(num) == 1:
            return True if num[0] in '018' else False
        if num[0] in strobo:
            return strobo[num[0]] == num[-1] and self.isStrobogrammatic(num[1:-1])
        else:
            return False

    #solution2, iterative solution
    def isStrobogrammatic2(self, num):
        strobo = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
        s, e = 0, len(num) - 1
        while s <= e:
            if num[s] not in strobo or strobo[num[s]] != num[e]:
                return False
            s += 1
            e -= 1
        return True
            

if __name__ == "__main__":
    sol = Solution()
    print sol.isStrobogrammatic("68189")
    print sol.isStrobogrammatic2("68189")
        
