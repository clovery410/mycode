class Solution(object):
    def multiply(self, num1, num2):
        num1 = num1[::-1]
        num2 = num2[::-1]
        res = ['0'] * (len(num1) + len(num2))
        for i in xrange(len(num1)):
            carry = 0
            for j in xrange(len(num2)):
                cur_res = int(num1[i]) * int(num2[j]) + carry + int(res[i+j])
                res[i+j] = str(cur_res % 10)
                carry = cur_res / 10
            if carry > 0:
                res[i+j+1] = str(carry)

        i = len(res) - 1
        while i > 0 and res[i] == '0':
            i -= 1
            res.pop()
    
        return ''.join(res[::-1])

    #solution2
    def multiply2(self, num1, num2):
        l1, l2 = len(num1), len(num2)
        res = [0] * (l1 + l2)
        for i in reversed(xrange(l1)):
            for j in reversed(xrange(l2)):
                mul_res = int(num1[i]) * int(num2[j])
                total = mul_res + res[i+j+1]
                res[i+j] += total / 10
                res[i+j+1] = total % 10
                
        string = ''.join(str(x) for x in res).lstrip('0')
        return string if len(string) > 0 else '0'
        

if __name__ == "__main__":
    sol = Solution()
    print sol.multiply2('0', '0')


        
