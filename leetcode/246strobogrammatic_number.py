class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        pair = {}
        pair['0'] = '0'
        pair['1'] = '1'
        pair['8'] = '8'
        pair['6'] = '9'
        pair['9'] = '6'
        
        l = len(num)
        i, j = 0, l - 1
        while i <= j:
            if num[i] not in pair or pair[num[i]] != num[j]:
                return False
            i += 1
            j -= 1
        return True


sol = Solution()
print sol.isStrobogrammatic('0168912')
