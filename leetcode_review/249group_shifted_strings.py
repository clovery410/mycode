import collections
class Solution(object):
    def groupStrings(self, strings):
        def getDeputy(string):
            deputy = ['a']
            l = len(string)
            for i in xrange(1, l):
                offset = (ord(string[i]) - ord(string[i-1]) + 26) % 26
                next_char = chr((ord(deputy[i-1]) + offset) % 26)
                deputy.append(next_char)
            return ''.join(deputy)
        
        groups = collections.defaultdict(list)
        for string in strings:
            deputy = getDeputy(string)
            groups[deputy].append(string)
            
        return [sorted(elem) for elem in groups.values()]

    #solution2, after looked at previous code, knowing that can just use offset as deputy, no need to construct the string
    def groupStrings2(self, strings):
        def getDeputy(string):
            deputy = ''
            for i in xrange(1, len(string)):
                deputy += str((ord(string[i]) - ord(string[i-1])) % 26)
            return deputy
            
        groups = collections.defaultdict(list)
        for string in strings:
            deputy = getDeputy(string)
            groups[deputy].append(string)
            
        return [sorted(elem) for elem in groups.values()]

if __name__ == "__main__":
    sol = Solution()
    strings = ["abc", "bcd", "acefsgdgdgd", "xyz", "az", "ba", "a", "z"]
    print sol.groupStrings(strings)
