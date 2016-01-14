class Solution(object):
    def groupAnagrams(self, strs):
        group = []
        record = {}
        for item in strs:
            candidate = tuple(sorted(item))
            if candidate not in record:
                record[candidate] = [item]
            else:
                record[candidate].append(item)

        for key in record:
            group.append(sorted(record[key]))

        return group

if __name__ == '__main__':
    string = ["eat", "tea", "tan", "ate", "nat", "bat"]
    sol = Solution()
    print sol.groupAnagrams(string)
            
