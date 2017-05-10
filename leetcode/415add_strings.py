class Solution(object):
    def addStrings(self, num1, num2):
        l1, l2 = len(num1), len(num2)
        res = [''] * max(l1, l2)

        carry = 0
        i, j = l1 - 1, l2 - 1
        for k in reversed(xrange(len(res))):
            m1 = num1[i] if i >= 0 else '0'
            m2 = num2[j] if j >= 0 else '0'
            num = ord(m1) - 48 + ord(m2) - 48 + carry
            res[k] = chr(num % 10 + 48)
            carry = num / 10
            i -= 1
            j -= 1
            
        if carry > 0:
            return '1' + ''.join(res)
        else:
            return ''.join(res)

    # follow-up: subtract strings
    def subStrings(self, num1, num2):
        def coreSub(num1, num2):
            l1, l2 = len(num1), len(num2)
            res = [''] * l1
            borrow = 0
            diff = 0
            i, j = l1 - 1, l2 - 1
            while i >= 0:
                m1 = ord(num1[i]) - 48
                m2 = ord(num2[j]) - 48 if j >= 0 else 0
                diff = m1 + 10 - m2 - borrow
                res[i] = chr(diff % 10 + 48)
                borrow = 1 if diff < 10 else 0
                j -= 1
                i -= 1
                
            k = 0
            while k < len(res) and res[k] == '0':
                res[k] = ''
            return ''.join(res)
            
        l1, l2 = len(num1), len(num2)
        if l1 > l2:
            return coreSub(num1, num2)
        elif l2 > l1:
            return '-' + coreSub(num2, num1)
        else:
            if num1 > num2:
                return coreSub(num1, num2)
            elif num1 < num2:
                return '-' + coreSub(num2, num1)
            else:
                return '0'

if __name__ == "__main__":
    sol = Solution()
    print sol.addStrings('9', '99')
    print sol.subStrings('100', '909')
