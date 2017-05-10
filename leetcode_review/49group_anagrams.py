import collections
class Solution(object):
    def groupAnagrams(self, strs):
        groups = collections.defaultdict(list)
        for word in strs:
            groups[''.join(sorted(word))].append(word)

        res = []
        for value in groups.values():
            res.append(sorted(value))
        return res

if __name__ == "__main__":
    sol = Solution()
    strs = ["eat","tea","tan","ate","nat","bat"]
    print sol.groupAnagrams(strs)
