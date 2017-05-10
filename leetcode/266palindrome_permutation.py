class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        record = {}
        count = 0
        for ch in s:
            if ch not in record:
                record[ch] = 1
                count += 1
            else:
                if record[ch] == 1:
                    count -= 1
                    record[ch] = 0
                else:
                    count += 1
                    record[ch] = 1
                    
        if count > 1:
            return False
        return True
