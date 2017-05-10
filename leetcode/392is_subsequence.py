class Solution(object):
    #solution1, use two pointers, just both begins at start, then scan
    def isSubsequence(self, s, t):
        idx = 0
        for i, c in enumerate(t):
            if idx == len(s):
                return True
            if s[idx] == c:
                idx += 1
        return True if idx == len(s) else False

    #solution2, scan at both sides
    def isSubsequence2(self, s, t):
        s1, e1 = 0, len(s) - 1
        s2, e2 = 0, len(t) - 1
        while s2 <= e2:
            if s1 > e1:
                return True
            if s[s1] == t[s2]:
                s1 += 1
            if s[e1] == t[e2]:
                e1 -= 1
            s2 += 1
            e2 -= 1
        return False

    #follow-up question, if there are lots of incoming S, say S1, S2,...,Sk, where k >= 1B
    #In this way, its better to prerecord all the index information in t
    def isSubsequenceMultiple(self, s, t):
        def binarySearch(lst, idx):
            s, e = 0, len(lst) - 1
            while s <= e:
                mid = (e - s) / 2 + s
                if lst[mid] > idx:
                    e = mid - 1
                else:
                    s = mid + 1
            return lst[s]
    
        maps = collections.defaultdict(list)
        #pre store all the index in t corresponding with a character
        for i, c in enumerate(t):
            maps[c].append(i)

        cur_idx = -1
        for c in s:
            if c not in maps or maps[c][-1] <= cur_idx:
                return False
            cur_idx = binarySearch(maps[c], cur_idx)
        return True

if __name__ == "__main__":
    sol = Solution()
    s = "axc"
    t = "ahbgdcd"
    print sol.isSubsequence(s, t)
    print sol.isSubsequence2(s, t)
