class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        idx = 0
        buf4 = [''] * 4
        
        while n > 0:
            cur_read_len = read4(buf4)
            for i in xrange(min(n, cur_read_len)):
                buf[idx] = buf4[i]
                n -= 1
                idx += 1
            if cur_read_len < 4:
                break
        return idx
