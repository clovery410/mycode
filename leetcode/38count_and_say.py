class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n <= 0:
            return ''
        res = '1'
        for i in xrange(2, n+1):
            res = self.getNext(res)
        return res
    
    def getNext(self, s):
        res = ''
        s += ' '
        pre_c, count = s[0], 1
        for curr_c in s[1:]:
            if curr_c != pre_c:
                res += str(count) + pre_c
                pre_c = curr_c
                count = 1
            else:
                count += 1
        return res
