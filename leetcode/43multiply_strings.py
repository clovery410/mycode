class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == '0' or num2 == '0':
            return '0'
        l1, l2 = len(num1), len(num2)
        res = ''
        curr = 0
        _num2 = int(num2)
        for i in reversed(xrange(l1)):
            curr += _num2 * int(num1[i])
            res = str(curr % 10) + res
            curr /= 10
        if curr:
            res = str(curr) + res
        return res

    #solution2
    def multiply2(self, num1, num2):
        if num1 == '0' or num2 == '0':
            return '0'
        l1, l2 = len(num1), len(num2)
        res = [0 for x in xrange(l1+l2)]
        curr_total = 0
        for i in reversed(xrange(l1)):
            for j in reversed(xrange(l2)):
                curr_mul = int(num1[i]) * int(num2[j])
                p1, p2 = i + j, i + j + 1
                curr_total = curr_mul + res[p2]
                res[p2] = curr_total % 10
                res[p1] += curr_total / 10
        return ''.join(res)
                
                
        
