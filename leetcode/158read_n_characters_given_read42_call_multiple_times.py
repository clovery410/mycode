# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def __init__(self):
        self.cache = collections.deque([])
        
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        idx = 0
        while self.cache and n > 0:
            buf[idx] = self.cache.popleft()
            idx += 1
            n -= 1

        buf4 = [''] * 4
        while n > 0:
            read_len = read4(buf4)
            # nothing to read
            if read_len == 0:
                break

            if read_len > n:
                self.cache += buf4[n:]
                
            for i in xrange(min(read_len, n)):
                buf[idx] = buf4[i]
                idx += 1
                n -= 1
            
        return idx
            
            
        
