class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        ret = []
        temp = sorted(strings)
        for word in temp:
            key = ''
            for i in xrange(1, len(word)):
                key += str((ord(word[i]) - ord(word[i-1])) % 26)
            if key not in dic:
                dic[key] = [word,]
            else:
                dic[key].append(word)
                
        for key in dic:
            ret.append(dic[key])
        return ret
